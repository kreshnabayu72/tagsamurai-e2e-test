---
id: TC-GS-TAG-E2E-056-delete-by-scan-gagal-server-dan-race-pair
title: "Delete by Scan: Gagal Server/Timeout T-23 dengan Scan Ulang Berhasil dan Tag Di-pair dari FAMS Tepat Sebelum Commit"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-TAG-360
  - TC-GS-TAG-361
coverage:
  web: automated
---

# Delete by Scan: Gagal Server/Timeout T-23 dengan Scan Ulang Berhasil dan Tag Di-pair dari FAMS Tepat Sebelum Commit

## Prerequisites

- Mode: FE+BE (backend nyata; kelas d harness scan hardware dengan fault injection kelas b lewat intercept di atas backend nyata). Spec ini menghapus data registri (DD-15 pada TC-GS-TAG-360, DD-17 pada TC-GS-TAG-361).
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite.
- Pemicu pair (P-2, sesi API, tidak diasersi): akun FAMS `famsAdmin_automated_qaTeam1@qwertysystem.net` (Admin FAMS Hendra Gunawan, Pre-setup TC), kredensial `Spectra.env.FA_ADMIN_PASSWORD`, hanya untuk mem-pair DD-16 ke aset pada TC-GS-TAG-361 (Q-5, Q-9; mekanisme dan endpoint tidak didefinisikan di TC, PRD, atau LLD).
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab All.
- Data Pre-setup: Seed Registri A (Client A, DD-01..DD-30). Baris yang dipakai: DD-15 `E28011606000020F00000001`, DD-16 `E28011606000020F00000002`, DD-17 `E28011606000020F00000003` (RFID Object Available, filler). Identifier tetap, tidak bisa bersufiks `{runId}` (S-12, Q-4); fixture BE memulihkan kondisi awal sebelum spec.
- Kemampuan teknis (disediakan tim FE/BE): simulasi reader RFID untuk sesi Delete by Scan (D-4, Q-1; mekanisme tidak didefinisikan di TC, PRD, atau LLD); intercept jaringan di atas backend nyata untuk request hapus tag hasil scan: respons 5xx, timeout, dan penahanan request hingga dilepas (endpoint tidak dinamai di TC; ditentukan tahap script dari `openapi.yaml`, S-13), dilepas segera sesudah dipakai (S-09); sesi API pair DD-16 ke aset tepat sesudah scan dan sebelum request dilepas (Q-5); pembacaan status registri lewat fixture BE selama sesi scan (halaman terkunci); seed dan reset idempotent Seed Registri A.
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): lepas intercept yang tersisa, unpair DD-16, dan kembalikan Seed Registri A lewat fixture BE.
- Suite serial (`parallel: false`). Spec tidak mengubah state global selain data registri dan sesi akun.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate`, lihat `suite.md`.

## Test Steps

### TC-GS-TAG-360: Server gagal atau timeout, scan ulang berhasil

1. Aktifkan intercept: request hapus tag dipaksa gagal 5xx
2. Klik `Delete by Scan` lalu pilih teknologi `RFID` pada overlay
3. Pindai DD-15 (request gagal 5xx)
4. Verifikasi toast error `Error, failed to delete TAG.`
5. Verifikasi tidak ada dialog
6. Tutup toast
7. Ganti intercept: request hapus ditahan hingga timeout
8. Pindai DD-16 (request timeout)
9. Verifikasi toast error `Error, failed to delete TAG.`
10. Verifikasi tidak ada dialog
11. Verifikasi DD-15 dan DD-16 tetap ada di registri (pembacaan lewat fixture BE)
12. Verifikasi sesi scan tetap aktif tanpa jeda
13. Lepas intercept (pulihkan jaringan)
14. Tutup toast
15. Pindai DD-15 lagi
16. Verifikasi toast sukses `Success, E28011606000020F00000001 has been deleted.`
17. Klik `Stop` pada widget

### TC-GS-TAG-361: Tag di-pair dari FAMS tepat sebelum commit scan

18. Aktifkan intercept: request hapus tag ditahan
19. Klik `Delete by Scan` lalu pilih teknologi `RFID` pada overlay
20. Pindai DD-16 (request hapus ditahan)
21. Pair tag DD-16 ke aset lewat sesi API akun FAMS hingga tersimpan
22. Lepaskan request yang ditahan, lalu lepas intercept
23. Verifikasi toast error `Error, this TAG is currently paired and can't be deleted.`
24. Verifikasi tidak ada dialog
25. Tutup toast
26. Verifikasi sesi scan berlanjut
27. Pindai DD-17
28. Verifikasi DD-17 langsung terhapus dengan toast sukses `Success, E28011606000020F00000003 has been deleted.`
29. Klik `Stop` pada widget
30. Verifikasi DD-16 tetap `Paired` di registri
31. Verifikasi DD-17 tidak ada di registri

## Notes

- Mode: FE+BE. Kelas d (hardware scan) dengan fault injection kelas b dan pemicu race. Subjudul `###` memetakan langkah ke id TC granular.
- Pengecualian P-5 butir b: TC-GS-TAG-360 adalah satu TC objek-uji ringan kelas b (satu kegagalan 5xx dan satu timeout pada sesi Delete by Scan) di spec dengan harness dominan yang sama permukaannya.
- Pengecualian P-2: intercept penahanan request dan pair DD-16 oleh akun FAMS (langkah 18, 21, 22) hanya memicu kondisi tag di-pair tepat sebelum commit; objek asersinya toast dan state di UI Global Settings. Intercept dilepas segera sesudah pemicu (langkah 13 dan 22; S-09).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 6, 14, dan 25 (menutup toast sebelum asersi toast berikutnya, S-09), 7 (mengganti jenis intercept dari 5xx ke timeout sesuai Langkah 3 TC), 13 dan 22 (melepas intercept).
- Asersi tambahan di luar Expected TC (S-03): tidak ada.
- Temuan untuk QA:
  - Q-1: kedua TC berlabel `Manual Only` (scan hardware atau dua sesi paralel); kemampuan simulasi reader dan sesi API dicatat di Prerequisites (D-4).
  - Q-5: pemicu "tepat sebelum commit" tidak deterministik dan mekanismenya tidak didefinisikan di TC; disediakan tim FE/BE.
  - Q-4: identifier tetap; kondisi Seed Registri A dipulihkan lewat fixture BE sebelum spec.
  - TC-GS-TAG-360 Expected a menyebut DD-15 dan DD-16 tetap di registri selama sesi scan aktif padahal halaman terkunci (page-lock) sehingga registri tidak teramati lewat UI; spec memakai pembacaan lewat fixture BE (langkah 11).
  - TC-GS-TAG-360 langkah 3 tidak menyebut cara membuat timeout (penundaan respons melampaui batas waktu FE); durasi tidak ditetapkan dan disediakan tim FE.
  - Post Condition TC-GS-TAG-360 butir a (DD-16 tetap Available) dan butir b (Event Log Success `1`), serta Post Condition TC-GS-TAG-361 butir b (Event Log: Success `1` dan tidak ada baris `Failed` untuk DD-16) tidak punya langkah observasi di TC dan tidak diasersi; butir a TC-GS-TAG-361 identik dengan Expected b dan c.

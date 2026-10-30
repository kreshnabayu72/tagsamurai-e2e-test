---
id: TC-GS-TAG-E2E-051-delete-efek-lintas-modul-fams-approvals-dan-tag-stock
title: "Delete: Efek Lintas Modul (Waiting for Approval di Approvals, Unit Stok Official, Unit Self-Purchased)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-145
  - TC-GS-TAG-187
  - TC-GS-TAG-347
coverage:
  web: automated
---

# Delete: Efek Lintas Modul (Waiting for Approval di Approvals, Unit Stok Official, Unit Self-Purchased)

## Prerequisites

- Mode: FE+BE (backend nyata). Spec ini menghapus data registri; seluruh aksi spec adalah Delete atas tiga baris berbeda (DD-03, DD-30, DD-12) yang dipulihkan lewat fixture BE.
- Akun aktor (ganti akun eksplisit; hasil di modul konsumen diasersi di sesi modul itu):
  - Principal approver (Mira Anggraini) `principalApprover_automated@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.GS_PRINCIPAL_TC_PASSWORD`, untuk Admin Console > Approvals > TAG Stock (TC-GS-TAG-145). Akun pertama spec: login di hook `before` spec ini. Kesamaan akun ini dengan env var terdaftar perlu dikonfirmasi tim FE saat tahap script (Q-2, kategori B).
  - Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.GS_TC_PASSWORD`, untuk Global Settings > TAG (aksi Delete). Hook `after` mengembalikan sesi ke akun ini sebagai default suite.
  - Akun Admin Console Client A untuk Admin Console > TAG Stock (TC-GS-TAG-187 dan 347): tidak ada di Pre-setup TC; akun dan kredensial disediakan tim FE (S-13).
- Layar awal: hook `beforeEach` membuka Admin Console > Approvals > TAG Stock Tab Active (akun pertama spec).
- Data Pre-setup: Seed Registri A (Client A, DD-01..DD-30; kartu RFID – Object TAG `21 of 50`). Target hapus: DD-03 `04A224B2C15E80` (Waiting for Approval, subject Activation Collision pending di Approvals > TAG Stock Tab Active), DD-30 `E28011606000020F00000016` (Official dari unit stok resmi In Use; precondition TC-GS-TAG-187, tidak diasersi selain Expected), DD-12 `E2801160600002054D8A0012` (Self-Purchased dengan unit stok di TAG Stock). Identifier tetap, tidak bisa bersufiks `{runId}` (S-12, Q-4); fixture BE memulihkan kondisi awal sebelum spec.
- Kemampuan teknis (disediakan tim FE/BE): seed dan reset idempotent Seed Registri A, unit stok resmi dan subject Activation Collision; pembacaan penanda event Delete selesai diproses (Eventual). Langkah dan selektor Approvals dan Admin Console TAG Stock tidak didefinisikan di TC, PRD, atau LLD (Q-9).
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): kembalikan Seed Registri A, unit stok, dan subject Approvals lewat fixture BE; sesi dikembalikan ke Total Control Client A.
- Suite serial (`parallel: false`). Spec tidak mengubah state global selain data di atas dan sesi akun.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate`, lihat `suite.md`.

## Test Steps

### TC-GS-TAG-145: Delete tag Waiting for Approval membatalkan subject

1. Verifikasi subject `Activation Collision` DD-03 tampil di Tab Active
2. Ganti akun ke Total Control Client A, buka Global Settings > TAG Tab All, catat nilai kartu NFC
3. Buka menu baris DD-03, lalu klik `Delete`
4. Klik `Delete` pada dialog
5. Verifikasi toast sukses `Success, TAG has been deleted.`
6. Verifikasi kartu NFC terpakai berkurang 1 dari nilai yang dicatat
7. Tunggu event Delete diproses (Eventual)

### TC-GS-TAG-187: Delete tag Official, unit stok kembali Available

8. Catat nilai kartu RFID – Object TAG
9. Buka menu baris DD-30, lalu klik `Delete`
10. Klik `Delete` pada dialog
11. Tunggu event Delete diproses (Eventual)
12. Verifikasi kartu RFID – Object TAG terpakai berkurang 1 dari nilai yang dicatat

### TC-GS-TAG-347: Delete tag Self-Purchased, unit stok terhapus

13. Catat nilai kartu RFID – Object TAG
14. Buka menu baris DD-12, lalu klik `Delete`
15. Klik `Delete` pada dialog
16. Tunggu event Delete diproses (Eventual)
17. Verifikasi kartu RFID – Object TAG terpakai berkurang 1 dari nilai yang dicatat

### TC-GS-TAG-187 dan TC-GS-TAG-347: unit stok di Admin Console TAG Stock

18. Ganti akun ke akun Admin Console Client A, buka Admin Console > TAG Stock, ketik Search `E28011606000020F00000016`, tekan Enter
19. Verifikasi unit stok DD-30 berstatus `Available`
20. Ganti isi kotak search dengan `E2801160600002054D8A0012`, tekan Enter
21. Verifikasi pencarian menampilkan `No results found` (unit tag DD-12 tidak ada lagi di TAG Stock)

### TC-GS-TAG-145: subject di Approvals sesudah Delete

22. Ganti akun ke Principal approver, buka Admin Console > Approvals > TAG Stock Tab Active
23. Verifikasi Tab Active tidak memuat subject DD-03
24. Klik Tab History
25. Verifikasi subject DD-03 tercatat di Tab History dengan Approval `Canceled` dan Approver `—`

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini 25 langkah, di bawah ambang sekitar 35. Tiga TC satu topik aksi (Delete tag dan efeknya di Approvals dan Admin Console TAG Stock) dengan satu dataset Seed Registri A dan tiga baris target berbeda; bagian sesudah tiap ganti akun tetap bermakna walau bagian sebelumnya gagal.
- Pemisahan: TC-GS-TAG-144 dan 371 (efek di Fixed Asset > TAG > To Be Returned, akun Admin FAMS, fixture aset terakhir dan pemulihan Seed Registri A penuh) ada di spec 098; blok FAMS itu mandiri dengan Prerequisites sendiri.
- Langkah ganti akun eksplisit: 2, 18, 22.
- Perubahan urutan (S-05 butir terakhir): urutan TC sumber (145, 187, 347) tetap pada blok penghapusan (langkah 1 sampai 17), tetapi verifikasi di Admin Console TAG Stock (TC-GS-TAG-187 dan 347, langkah 18 sampai 21) dan Approvals (TC-GS-TAG-145, langkah 22 sampai 25) dikelompokkan sesudah ketiga Delete supaya ganti akun hanya tiga kali. Principal approver membuka Tab Active lebih dulu (langkah 1) karena subject harus terlihat sebelum DD-03 dihapus.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 2 (bagian mencatat kartu NFC), 8, dan 13 (mencatat baseline kartu), 7, 11, dan 16 (menunggu event Delete diproses, bukan asersi), 2, 18, dan 22 (ganti akun dan navigasi), 24 (membuka Tab History).
- Asersi tambahan di luar Expected TC (S-03): langkah 1 (anchor positif sebelum absence langkah 23, S-02 butir 2; precondition TC-GS-TAG-145); langkah 5 memakai toast `Success, TAG has been deleted.` yang ditetapkan TC-GS-TAG-142 sebagai teks toast Delete tag.
- Rujukan: TC-GS-TAG-142 dan 143 (Delete sukses per status dan kuota kartu) ada di spec 050; TC-GS-TAG-144 dan 371 ada di spec 098.
- Temuan untuk QA:
  - Q-9: langkah dan selektor di Approvals dan Admin Console TAG Stock tidak didefinisikan; verifikasi di modul konsumen hanya sejauh Expected TC.
  - Q-2: Pre-setup TC memakai `principalApprover_automated`, sedangkan `.env.example` mendaftarkan `totalControlPrincipal_automated_qaTeam1` (GS_PRINCIPAL_TC); kesamaan akun perlu dikonfirmasi tim FE saat tahap script (kategori B).
  - TC-GS-TAG-145 tidak menyebut akun yang membuka Admin Console > Approvals; spec memakai Principal approver. TC-GS-TAG-187 dan 347 menyebut "akun Admin Console Client A tersedia" tanpa email.
  - TC-GS-TAG-187 tidak punya Expected toast; TC-GS-TAG-145 Expected a menyebut "Toast sukses" tanpa teks (spec memakai `Success, TAG has been deleted.` dari TC-GS-TAG-142).
  - Post Condition TC-GS-TAG-145 butir a, b, dan c identik dengan Expected a dan b.
  - Q-4: identifier tetap; fixture BE memulihkan Seed Registri A sebelum spec.

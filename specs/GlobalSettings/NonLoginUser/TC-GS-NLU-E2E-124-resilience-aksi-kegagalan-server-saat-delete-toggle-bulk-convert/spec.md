---
id: TC-GS-NLU-E2E-124-resilience-aksi-kegagalan-server-saat-delete-toggle-bulk-convert
title: "Resilience aksi: kegagalan server saat Delete, Toggle, Bulk Convert, Convert"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-195
  - TC-GS-NLU-213
  - TC-GS-NLU-231
  - TC-GS-NLU-241
coverage:
  web: automated
---

# Resilience aksi: kegagalan server saat Delete, Toggle, Bulk Convert, Convert

## Prerequisites

- Mode: FE+BE. Spec memaksa respons 500 pada request aksi lewat `Spectra.intercept()` di atas backend nyata; hasil retry dan state data diasersi dari backend nyata.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Kemampuan teknis: `Spectra.intercept()` untuk memaksa respons 500 pada request yang disebut tiap langkah, parsial di atas backend nyata (bagian 6); nama endpoint ditentukan tim FE pada tahap script (S-13). Hook `after` melepas semua intercept walau spec gagal di tengah.
- Data Pre-setup No. 9 (Position `Contractor`, `Driver`, `Field Technician`; Division `Operations`; Login User `Ahmad Fauzi`) hanya dibaca.
- Request yang dipaksa 500: status Deactivate dan Activate (TC-GS-NLU-213), Bulk Convert (TC-GS-NLU-231), Convert row (TC-GS-NLU-241), dan Delete (TC-GS-NLU-195), satu per satu.
- Data milik spec (di-seed hook `before` lewat API, dibersihkan hook `after`; mekanisme seeding dan penghapusan disediakan tim FE/BE; Division `Operations`, Represented By `Ahmad Fauzi`, Email `<nama>+{runId}-124@qwertysystem.net`):
  - `Rina Marlina {runId}-124` (Active, Position `Driver`) dan `Joko Susilo Dua {runId}-124` (Inactive manual, Position `Contractor`) untuk TC-GS-NLU-213.
  - `Budi Kurniawan {runId}-124` (Active, Position `Field Technician`) dan `Siti Rahayu {runId}-124` (Active, tanpa Position dan Employee ID) untuk TC-GS-NLU-231.
  - `Rani Lestari {runId}-124` (Active, Email `rani.lestari+{runId}-124@qwertysystem.net`) untuk TC-GS-NLU-241.
  - `Joko Susilo {runId}-124` (Inactive manual, Position `Contractor`) untuk TC-GS-NLU-195.
- Pemulihan: hook `after` melepas intercept dan menghapus lewat API semua data `{runId}-124` yang tersisa (termasuk Login User hasil Convert).
- Suite berjalan serial (`parallel: false`).
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.

## Test Steps

### TC-GS-NLU-213: Kegagalan server pada Deactivate dan Activate mengembalikan switch

1. Pasang intercept yang memaksa respons 500 untuk request ubah status
2. Ketik Search `{runId}-124`, tekan Enter, klik switch Active baris `Rina Marlina {runId}-124` (ON)
3. Klik `[Deactivate]` pada dialog konfirmasi
4. Verifikasi Toast error `Error, failed to deactivate non-login user.`
5. Verifikasi switch Active baris `Rina Marlina {runId}-124` kembali ON
6. Klik switch Active baris `Joko Susilo Dua {runId}-124` (OFF)
7. Klik `[Activate]` pada dialog konfirmasi
8. Verifikasi Toast error `Error, failed to activate non-login user.`
9. Verifikasi switch Active baris `Joko Susilo Dua {runId}-124` kembali OFF
10. Lepas intercept (pulihkan response)

### TC-GS-NLU-231: Kegagalan server pada Bulk Convert menyisakan baris tetap Non-Login User

11. Pasang intercept yang memaksa respons 500 untuk request Convert
12. Centang baris `Budi Kurniawan {runId}-124` dan `Siti Rahayu {runId}-124`
13. Pilih `Bulk Action` > `Convert to Login User`
14. Klik `[Convert]`
15. Verifikasi Toast error `Error, failed to convert non-login user.`
16. Tunggu list di-refresh oleh aplikasi
17. Verifikasi baris `Budi Kurniawan {runId}-124` dan `Siti Rahayu {runId}-124` tetap Non-Login User di tabel
18. Verifikasi seleksi kedua baris dipertahankan
19. Lepas intercept (pulihkan response)
20. Pilih `Bulk Action` > `Convert to Login User`
21. Klik `[Convert]`
22. Tunggu aksi selesai (dialog Convert menutup)
23. Verifikasi baris `Budi Kurniawan {runId}-124` dan `Siti Rahayu {runId}-124` hilang dari tabel Non-Login User (retry berhasil)

### TC-GS-NLU-241: Kegagalan server pada Convert row menampilkan toast error

24. Pasang intercept yang memaksa respons 500 untuk request Convert
25. Ketik Search `Rani Lestari {runId}-124`, tekan Enter, klik `⋯` baris `Rani Lestari {runId}-124` > `Convert to Login User`
26. Klik `[Convert]`
27. Verifikasi Toast error `Error, failed to convert non-login user.`
28. Verifikasi baris `Rani Lestari {runId}-124` tetap Non-Login User di tabel
29. Lepas intercept (pulihkan response)
30. Klik `⋯` baris `Rani Lestari {runId}-124` > `Convert to Login User`, lalu klik `[Convert]` (retry)
31. Tunggu aksi selesai (dialog Convert menutup)
32. Verifikasi baris `Rani Lestari {runId}-124` hilang dari tabel Non-Login User (retry berhasil)

### TC-GS-NLU-195: Kegagalan server saat Delete mempertahankan baris dan menampilkan toast error

33. Pasang intercept yang memaksa respons 500 untuk request Delete
34. Ketik Search `Joko Susilo {runId}-124`, tekan Enter, klik `⋯` baris `Joko Susilo {runId}-124` > `Delete`
35. Klik `[Delete]` pada dialog konfirmasi
36. Verifikasi Toast error `Error, failed to delete non-login user.`
37. Verifikasi baris `Joko Susilo {runId}-124` tetap ada di tabel
38. Lepas intercept (pulihkan response)
39. Klik `⋯` baris `Joko Susilo {runId}-124` > `Delete`, lalu klik `[Delete]` pada dialog konfirmasi (retry)
40. Verifikasi Toast sukses `Success, non-login user has been deleted.`
41. Verifikasi baris `Joko Susilo {runId}-124` hilang dari tabel

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Kelas b (fault injection): intercept parsial di atas backend nyata; intercept dilepas pada langkah 10, 19, 29, dan 38 sebelum retry, dan hook `after` melepas sisa intercept (S-09).
- Urutan TC dalam spec: TC-GS-NLU-213, 231, 241, 195. TC-GS-NLU-195 (Delete) diletakkan terakhir karena aksi menghapus data di akhir spec (S-10).
- Langkah penghubung (S-03, R-16): langkah 2 (Search record yang dicari), langkah 1, 11, 24, 33 (memasang intercept), langkah 16, 22, 31 (menunggu list di-refresh atau aksi selesai), langkah 10, 19, 29, 38 (melepas intercept).
- Di atas 35 langkah, alasan: Alasan jumlah langkah: nominal 41 langkah. Semua blok kelas b dengan pola identik (paksa 500 pada satu aksi, amati toast dan state, lepas, retry), tiap blok memakai record milik sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; kegagalan Download ada di spec 138.
- Temuan untuk QA:
  - TC-GS-NLU-213 langkah 3 menulis "Pulihkan response; klik switch Joko Susilo ... dengan response gagal" yang kontradiktif; spec mempertahankan intercept 500 untuk kedua aksi (Deactivate dan Activate) dan melepasnya sesudahnya.
  - TC-GS-NLU-195 tidak menyebut apakah dialog Delete tertutup sesudah error; spec membuka menu `⋯` dan dialog Delete lagi untuk retry.
  - TC-GS-NLU-231 menyebut "list di-refresh" tanpa langkah pemicu; spec menunggu refresh otomatis aplikasi dan tidak memuat ulang halaman supaya seleksi dapat diamati.
  - TC-GS-NLU-195, 213, 231, dan 241 memakai Joko Susilo, Rina Marlina, Budi Kurniawan, Siti Rahayu, dan Rani Lestari Pre-setup; spec memakai record milik spec yang setara (S-06).

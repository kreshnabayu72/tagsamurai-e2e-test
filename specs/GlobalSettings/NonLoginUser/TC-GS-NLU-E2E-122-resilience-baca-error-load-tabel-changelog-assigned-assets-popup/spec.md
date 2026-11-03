---
id: TC-GS-NLU-E2E-122-resilience-baca-error-load-tabel-changelog-assigned-assets-popup
title: "Resilience baca: error load tabel, changelog, Assigned Assets, Popup Select User, Borrowed Assets"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-11
  - TC-GS-NLU-376
  - TC-GS-NLU-477
coverage:
  web: automated
---

# Resilience baca: error load tabel, changelog, Assigned Assets, Popup Select User, Borrowed Assets

## Prerequisites

- Mode: FE+BE. Spec memaksa respons 500 sebagian lewat `Spectra.intercept()` di atas backend nyata; data berasal dari backend nyata.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Kemampuan teknis: `Spectra.intercept()` untuk memaksa respons 500 pada request yang disebut tiap langkah, parsial di atas backend nyata (bagian 6); nama endpoint ditentukan tim FE pada tahap script (S-13). Hook `after` melepas semua intercept walau spec gagal di tengah.
- Data Pre-setup No. 9 sampai 13 (Position `Driver` dan `Manager`; Division `Operations`, `Warehouse`, `Logistics`, `Finance`; Login User `Ahmad Fauzi` dan `Dewi Anggraini`; Custom Field dasar) hanya dibaca, tidak diubah atau dihapus.
- Request yang dipaksa 500 (satu per satu, dilepas segera sesudah dipakai): list Non-Login User (TC-GS-NLU-11), Borrowed Assets Detail (TC-GS-NLU-376), Changelog agregat, Changelog Detail, Assigned Assets, dan list Popup Select User (TC-GS-NLU-477).
- Data milik spec (di-seed hook `before` lewat API, dibersihkan hook `after`; mekanisme seeding, penghapusan, dan transaksi FAMS disediakan tim FE/BE): `Budi Resilien {runId}-122` (First Name `Budi`, Last Name `Resilien {runId}-122`, Division `Operations`, Email `budiresilien+{runId}-122@qwertysystem.net`, Represented By `Ahmad Fauzi`, Active) dengan transaksi Borrowed `BRW-20260610-0001` (Laptop - 1) dan Assigned `ASG-20260505-0001` (Company Vehicle B1234XY) seperti Tabel Data Uji Pre-setup No. 14, serta satu entri Changelog (`Create`) dari seeding.
- Pemulihan: hook `after` melepas intercept dan menghapus lewat API semua data `{runId}-122` yang tersisa.
- Suite berjalan serial (`parallel: false`).
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.

## Test Steps

### TC-GS-NLU-11: Error load tabel Non-Login User dan pemulihan lewat Try Again

1. Pasang intercept yang memaksa respons 500 untuk request list Non-Login User
2. Muat ulang halaman dengan F5 pada sub-tab Non-Login User
3. Verifikasi area tabel menampilkan pesan `Unable to load this data.` dan tombol `[Try Again]`
4. Verifikasi area tabel tidak menampilkan empty state
5. Lepas intercept (pulihkan response)
6. Klik `[Try Again]`
7. Verifikasi baris data tampil di tabel

### TC-GS-NLU-376: Error load sub-tab Borrowed Assets dan pemulihan

8. Ketik Search `Budi Resilien {runId}-122`, tekan Enter, klik Name baris tersebut untuk membuka Detail
9. Pasang intercept yang memaksa respons 500 untuk request Borrowed Assets
10. Klik tab `Responsibilities`, sub-tab `Borrowed Assets`
11. Verifikasi area tabel menampilkan pesan `Unable to load this data.` dan tombol `[Try Again]`
12. Verifikasi area tabel tidak menampilkan empty state
13. Lepas intercept (pulihkan response)
14. Klik `[Try Again]`
15. Verifikasi baris Borrowed Assets tampil

### TC-GS-NLU-477: Error load Modal Changelog agregat, Tab Changelog Detail, Assigned Assets, dan Popup Select User

16. Kembali ke List Non-Login User lewat sidebar
17. Pasang intercept yang memaksa respons 500 untuk request Changelog agregat
18. Klik icon `Changelog` pada Table Tools
19. Verifikasi Modal Changelog agregat menampilkan pesan `Unable to load this data.` dan tombol `[Try Again]`
20. Verifikasi Modal Changelog agregat tidak menampilkan empty state
21. Lepas intercept (pulihkan response)
22. Klik `[Try Again]`
23. Verifikasi baris Modal Changelog agregat tampil
24. Tutup Modal Changelog dengan `✕`, lalu ketik Search `Budi Resilien {runId}-122`, tekan Enter, klik Name baris tersebut untuk membuka Detail
25. Pasang intercept yang memaksa respons 500 untuk request Changelog Detail
26. Klik tab `Changelog`
27. Verifikasi Tab Changelog Detail menampilkan pesan `Unable to load this data.` dan tombol `[Try Again]`
28. Verifikasi Tab Changelog Detail tidak menampilkan empty state
29. Lepas intercept (pulihkan response)
30. Klik `[Try Again]`
31. Verifikasi baris Tab Changelog Detail tampil
32. Pasang intercept yang memaksa respons 500 untuk request Assigned Assets
33. Klik tab `Responsibilities`, sub-tab `Assigned Assets`
34. Verifikasi sub-tab Assigned Assets menampilkan pesan `Unable to load this data.` dan tombol `[Try Again]`
35. Verifikasi sub-tab Assigned Assets tidak menampilkan empty state
36. Lepas intercept (pulihkan response)
37. Klik `[Try Again]`
38. Verifikasi baris Assigned Assets tampil
39. Kembali ke List Non-Login User lewat sidebar
40. Pasang intercept yang memaksa respons 500 untuk request list Popup Select User
41. Klik `[+ Non-Login User]`, lalu klik `[+ Select User]`
42. Verifikasi Popup Select User menampilkan pesan `Unable to load this data.` dan tombol `[Try Again]`
43. Verifikasi Popup Select User tidak menampilkan empty state
44. Lepas intercept (pulihkan response)
45. Klik `[Try Again]`
46. Verifikasi baris Popup Select User tampil
47. Tutup Popup Select User dan popup Create dengan `✕` (tanpa perubahan, tanpa dialog `Unsaved Changes`)

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Kelas b (fault injection): intercept parsial di atas backend nyata (bagian 6 dan 3 prinsip 13b); intercept dilepas segera sesudah tiap blok (S-09).
- Langkah penghubung (S-03, R-16): langkah 8, 24 (Search record yang dicari dan membuka Detail), langkah 16, 39 (kembali ke List lewat sidebar), dan langkah 47 (menutup popup yang belum diubah).
- Di atas 35 langkah, alasan: Alasan jumlah langkah: nominal 47 langkah. Semua blok kelas b dengan pola identik (paksa 500, amati pesan dan tombol, lepas, `[Try Again]`) pada enam surface berbeda; satu spec per kelas ringan per modul (bagian 3 prinsip 13), dan kegagalan satu blok tidak membuat blok lain kehilangan makna karena tiap blok memasang dan melepas intercept sendiri.
- TC-GS-NLU-477 memuat empat surface dalam satu TC sehingga tetap satu spec (satu TC satu spec).
- Temuan untuk QA:
  - TC-GS-NLU-11, 376, dan 477 menyebut Budi Kurniawan dan data Pre-setup; spec memakai record milik spec `Budi Resilien {runId}-122` supaya tidak bergantung pada data bersama (S-06).
  - TC-GS-NLU-477 langkah 7 membuka Popup Select User dari Popup Create tanpa mengisi field; spec menutup kedua popup tanpa dialog `Unsaved Changes` karena tidak ada field yang diubah.

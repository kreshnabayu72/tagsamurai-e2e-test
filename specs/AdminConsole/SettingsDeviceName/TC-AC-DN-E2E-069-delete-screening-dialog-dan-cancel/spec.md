---
id: TC-AC-DN-E2E-069-delete-screening-dialog-dan-cancel
title: "Delete Device Name: Screening Row Action dan Dialog Konfirmasi, Backdrop, Esc, dan Cancel"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-181
  - TC-AC-DN-182
  - TC-AC-DN-183
  - TC-AC-DN-184
  - TC-AC-DN-185
coverage:
  web: automated
---

# Delete Device Name: Screening Row Action dan Dialog Konfirmasi, Backdrop, Esc, dan Cancel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`; email dirujuk lewat `Fixture.settings-device-name`, belum ada, disediakan tim FE), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): hook `beforeEach` suite membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip disetel `seen` oleh hook `before` suite dan dipulihkan di `after`.
- Data Pre-setup (baca-saja, nilai dirujuk lewat `Fixture.settings-device-name`): #16 Device Name inti, baris `Cable Tester` (Category `Accessory`, Measurement `Unit`, tanpa SKU, tanpa unit BYO). Spec hanya membuka overlay dan dialog lalu membatalkannya, sehingga baris Pre-setup tidak diubah dan Last Modified-nya tidak berubah (S-06).
- Env var yang dipakai: `AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`).

## Test Steps

### TC-AC-DN-181: Screening Overlay Row Action

1. Klik ikon aksi pada kolom Actions baris `Cable Tester`
2. Verifikasi Overlay Row Action menampilkan opsi berurutan `Detail` (ikon FileInfoLine, severity dark), `Edit` (ikon Edit2Line, severity dark), `Delete` (ikon DeleteBin6Line, severity danger)
3. Verifikasi opsi `Detail` dan `Edit` berada di atas `Delete` (kelompok dark lebih dulu daripada danger)
4. Tekan Esc untuk menutup Overlay Row Action

### TC-AC-DN-182: Screening dialog konfirmasi Delete single untuk Device Name bersih

5. Ketik Search `Cable Tester`, tekan Enter
6. Klik ikon aksi pada kolom Actions baris `Cable Tester` lalu klik `Delete`
7. Verifikasi judul dialog "Delete Device Name" tanpa tanda tanya
8. Verifikasi body: baris pertama bullet terisolasi `Cable Tester`
9. Verifikasi body: kalimat penutup `Are you sure you want to delete it? This action cannot be undone.`
10. Verifikasi footer: tombol `[Cancel]` (varian text, severity contrast) dan tombol `[Delete]` (severity danger)

### TC-AC-DN-183: Klik backdrop pada dialog konfirmasi Delete single tidak menutup dialog

11. Klik area gelap di luar dialog
12. Verifikasi dialog `Delete Device Name` tetap terbuka dengan bullet `Cable Tester`
13. Verifikasi tidak ada toast
14. Verifikasi baris `Cable Tester` tetap ada pada List di belakang dialog

### TC-AC-DN-184: Tekan Esc pada dialog konfirmasi Delete single setara tombol Cancel

15. Tekan Esc
16. Verifikasi dialog tertutup dan pengguna kembali ke List
17. Verifikasi tidak ada toast
18. Verifikasi baris `Cable Tester` tetap ada pada List

### TC-AC-DN-185: Klik Cancel pada dialog konfirmasi Delete single membatalkan penghapusan

19. Klik ikon aksi pada kolom Actions baris `Cable Tester` lalu klik `Delete`
20. Klik `[Cancel]`
21. Verifikasi dialog tertutup
22. Verifikasi tidak ada toast
23. Verifikasi baris `Cable Tester` tetap ada pada List dengan Category `Accessory` dan Measurement `Unit`
24. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 4 (menutup Overlay Row Action) dan langkah 24 (mengosongkan Search agar List kembali penuh).
- Halaman yang sama dipakai berulang tanpa submit: TC-AC-DN-183 dan TC-AC-DN-184 melanjutkan dialog Delete yang sudah terbuka pada TC-AC-DN-182 (langkah 11 dan seterusnya); TC-AC-DN-185 membuka dialog lagi pada langkah 19 karena dialog sudah ditutup pada TC-AC-DN-184. Search `Cable Tester` dari langkah 5 tetap aktif.
- Baris Pre-setup `Cable Tester` dipakai karena semua aksi dibatalkan atau tidak menghapus (S-06); tidak ada data yang diubah.
- Temuan untuk QA:
  - TC-AC-DN-185 Post Condition ("Record `Cable Tester` tetap tersimpan", "Tidak ada entri log baru") tidak punya langkah observasi di TC, sehingga tidak diasersi.
  - TC-AC-DN-181 menyebut nama ikon komponen (FileInfoLine, Edit2Line, DeleteBin6Line) tanpa menyatakan cara pengamatannya; cara membaca ikon diserahkan ke Page Object.

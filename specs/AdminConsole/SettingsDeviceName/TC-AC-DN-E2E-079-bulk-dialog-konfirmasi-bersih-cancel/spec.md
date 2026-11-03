---
id: TC-AC-DN-E2E-079-bulk-dialog-konfirmasi-bersih-cancel
title: "Bulk Delete: Dialog Konfirmasi Item Bersih, Cancel, Esc, dan Backdrop"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-219
  - TC-AC-DN-220
  - TC-AC-DN-221
  - TC-AC-DN-222
coverage:
  web: automated
---

# Bulk Delete: Dialog Konfirmasi Item Bersih, Cancel, Esc, dan Backdrop

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`; email dirujuk lewat `Fixture.settings-device-name`, belum ada, disediakan tim FE), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): hook `beforeEach` suite membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip disetel `seen` oleh hook `before` suite dan dipulihkan di `after`.
- Data Pre-setup (baca-saja, nilai dirujuk lewat `Fixture.settings-device-name`): #16 `Cable Tester` dan `Door Antenna` (tanpa SKU, tanpa unit BYO). Dialog hanya dibuka lalu dibatalkan, sehingga baris Pre-setup tidak diubah dan Last Modified-nya tidak berubah (S-06).
- Env var yang dipakai: `AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`).

## Test Steps

### TC-AC-DN-219: Screening dialog konfirmasi Bulk Delete saat seluruh item bersih

1. Centang checkbox baris `Cable Tester` dan `Door Antenna`
2. Klik `Bulk Action` lalu `Delete`
3. Verifikasi judul dialog "Delete Device Names"
4. Verifikasi body: bullet `Cable Tester` dan `Door Antenna`
5. Verifikasi body: bullet berada dalam container yang dapat di-scroll tanpa ringkasan jumlah
6. Verifikasi body: kalimat penutup `Are you sure you want to delete them? This action cannot be undone.`
7. Verifikasi footer: tombol `[Cancel]` (varian text, severity contrast) dan tombol `[Delete]` (severity danger)

### TC-AC-DN-220: Cancel pada dialog Bulk Delete mempertahankan seleksi

8. Klik `[Cancel]`
9. Verifikasi dialog tertutup
10. Verifikasi tidak ada toast
11. Verifikasi Bulk Action Bar tetap tampil dengan `2 Device Names selected`
12. Verifikasi baris `Cable Tester` dan `Door Antenna` tetap tercentang dan tidak terhapus

### TC-AC-DN-221: Esc pada dialog Bulk Delete setara Cancel

13. Klik `Bulk Action` lalu `Delete`
14. Tekan tombol Esc
15. Verifikasi dialog tertutup
16. Verifikasi tidak ada toast
17. Verifikasi seleksi `2 Device Names selected` dipertahankan
18. Verifikasi tidak ada Device Name yang terhapus

### TC-AC-DN-222: Klik backdrop pada dialog Bulk Delete tidak menutup dialog

19. Klik `Bulk Action` lalu `Delete`
20. Klik area gelap di luar dialog
21. Verifikasi dialog `Delete Device Names` tetap terbuka dengan bullet `Cable Tester` dan `Door Antenna`
22. Verifikasi tidak ada toast
23. Klik `[Cancel]`
24. Klik ikon `(X)` pada Bulk Action Bar

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Halaman yang sama dipakai berulang tanpa submit: TC-AC-DN-220, 221, dan 222 memakai seleksi `Cable Tester` dan `Door Antenna` yang dibuat pada TC-AC-DN-219 (langkah awal TC itu identik) dan dialog dibuka ulang dari seleksi yang dipertahankan.
- Langkah penghubung (S-03, S-09): langkah 23 (menutup dialog) dan langkah 24 (membersihkan seleksi).
- Baris Pre-setup dipakai karena semua aksi dibatalkan (S-06).
- Temuan untuk QA: TC-AC-DN-221 Expected butir c ("Tidak ada Device Name yang terhapus") dan TC-AC-DN-220 butir c memakai baris tetap ada sebagai bukti; Post Condition tidak ada.

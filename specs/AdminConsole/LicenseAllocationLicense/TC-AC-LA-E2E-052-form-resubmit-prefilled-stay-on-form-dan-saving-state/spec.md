---
id: TC-AC-LA-E2E-052-form-resubmit-prefilled-stay-on-form-dan-saving-state
title: "Form Resubmit Pre-filled, Stay on this Form, Tanpa Stay, dan Saving State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-182
  - TC-AC-LA-185
  - TC-AC-LA-186
  - TC-AC-LA-187
coverage:
  web: automated
---

# Form Resubmit Pre-filled, Stay on this Form, Tanpa Stay, dan Saving State

## Prerequisites

- Mode: FE+BE. Respons submit ditahan lewat `Spectra.intercept()` di atas backend nyata (TC-AC-LA-187); selebihnya memakai backend nyata.
- Akun aktor: Distributor Create+Read+Update `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Pre-setup #4), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > License Allocation, tab Current). Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen` oleh hook suite, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup (hanya dibaca): PT Sejahtera (#19, `SUBS-20260101-A1B2C`), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (#33), Product Price (#34: Concurrent User $365 per unit per tahun). Toggle Require Approval for Allocation OFF (#39), diatur fixture backend (disediakan tim FE/BE) di hook `before` dan dipulihkan di hook `after`.
- Data Dinamis: alokasi `Canceled` manual Concurrent User +5 ke PT Sejahtera milik `Dewi A`, di-seed lewat API di hook `before` (milik spec ini, bukan baris Pre-setup #48 bersama; Allocation ID dibaca dari hasil seeding); serta tiga alokasi Completed Active Concurrent User +2 ke PT Sejahtera dari TC-AC-LA-185, 186, dan 187. Alokasi tidak dapat dihapus (tanpa Delete); saldo kantong dan ledger kuota dipulihkan oleh baseline automation dan fixture backend di hook `after`.
- Baseline: daftar Allocation ID baris di halaman pertama tab Current dicatat sebelum tiap `[Submit]` (langkah 11, 22, dan 28).
- Kemampuan teknis: `Spectra.intercept()` untuk menunda respons submit 5 detik lalu melepasnya; menghitung jumlah request submit yang terkirim.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-182: Form pre-filled dari Resubmit memakai dirty-guard dengan nilai awal sebagai pristine

1. Buka Allocation > License Allocation tab History
2. Ketik Search Allocation ID alokasi Canceled seed milik spec, tekan Enter
3. Klik `Resubmit` pada baris Canceled
4. Tekan `Esc` tanpa mengubah apa pun
5. Verifikasi form tertutup tanpa dialog D-02
6. Klik `Resubmit` pada baris Canceled yang sama
7. Ubah Additional Quantity, lalu tekan `Esc`
8. Verifikasi dialog D-02 `Unsaved Changes` tampil
9. Klik `[Leave]`
10. Klik `(←)` pada kotak Search, lalu buka tab Current

### TC-AC-LA-185: Stay on this form, Client dan Target dipertahankan, Type, Current Quota, dan Quantity direset

11. Catat baseline Allocation ID baris di halaman pertama tab Current
12. Klik `[+ Allocation]`
13. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, isi Additional Quantity `2`
14. Centang `Stay on this form after submitting`
15. Klik `[Submit]`
16. Verifikasi toast sukses "Success, license has been allocated."
17. Verifikasi form tetap terbuka dengan Client `PT Sejahtera` dan Target `SUBS-20260101-A1B2C` dipertahankan
18. Verifikasi Type, Current Quota, dan Additional Quantity di-reset dan form kembali pristine
19. Verifikasi daftar List di belakang modal diperbarui dengan baris baru (Allocation ID tidak ada pada baseline langkah 11)
20. Tekan `Esc`
21. Verifikasi form tertutup langsung tanpa dialog D-02 karena sudah pristine

### TC-AC-LA-186: Tanpa Stay, setelah Submit sukses modal tertutup dan List diperbarui

22. Catat baseline Allocation ID baris di halaman pertama tab Current
23. Klik `[+ Allocation]`
24. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, isi Additional Quantity `2`, dan biarkan Stay tidak dicentang
25. Klik `[Submit]`
26. Verifikasi toast sukses "Success, license has been allocated."
27. Verifikasi modal tertutup dan baris baru tampil di tab Current (Allocation ID tidak ada pada baseline langkah 22)

### TC-AC-LA-187: Tombol Submit disabled dan loading selama request berjalan

28. Catat baseline Allocation ID baris di halaman pertama tab Current
29. Klik `[+ Allocation]`
30. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, isi Additional Quantity `2`
31. Atur intercept: tunda 5 detik respons submit
32. Klik `[Submit]`
33. Verifikasi `[Submit]` menampilkan loading dan disabled, serta `[Clear Field]` dan `[✕]` disabled
34. Klik `[Submit]`, `[Clear Field]`, dan `[✕]` selama menunggu
35. Lepas tahanan respons submit dan lepas intercept
36. Verifikasi hanya satu request submit terkirim
37. Verifikasi hanya satu record tercipta (satu baris baru, Allocation ID tidak ada pada baseline langkah 28)

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Buka form 5 kali, kejadian menutup 5 (langkah 4, 7 sampai 9, 20, 25, dan 32 sampai 35).
- Spec 37 langkah, di atas smell 35 langkah, dengan empat blok satu topik (perilaku form Allocate setelah dan selama Submit, serta Resubmit pre-filled) yang berdiri sendiri: tiap blok memakai state sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna, sehingga tidak dipecah.
- Penyimpangan data (S-06): TC-AC-LA-182 memakai baris Pre-setup #48 bersama; spec memakai seed Canceled milik spec dengan keadaan yang sama agar Pre-setup bersama tidak berubah.
- Langkah penghubung (S-03): langkah 1 sampai 2 (pindah ke tab History dan Search untuk menemukan baris target, R-16), langkah 10 (mengosongkan Search dan kembali ke tab Current), langkah 11, 22, dan 28 (baseline), langkah 31 dan 35 (menahan dan melepas respons).
- Temuan untuk QA:
  - TC-AC-LA-182 Langkah 2 ("Tekan `Esc` tanpa mengubah apa pun") dan Langkah 3 ("ubah Additional Quantity, tekan `Esc`") tidak menyebut tombol penutup dialog D-02; spec menutup form lewat `[Leave]` sesuai S-08 setelah memverifikasi dialog.
  - TC-AC-LA-185 Expected d ("Daftar List di belakang modal diperbarui") hanya dapat diamati bila daftar terlihat di balik modal; spec mengasersi baris baru pada daftar.
  - TC-AC-LA-187 Expected b ("Hanya satu request terkirim dan satu record tercipta") tidak menyebut cara menghitung request; spec memakai intercept untuk menghitung request submit dan daftar sebagai bukti satu record.
  - TC-AC-LA-187 Post Condition ("Satu record") diwakili oleh Expected b; tidak ada langkah observasi tambahan.

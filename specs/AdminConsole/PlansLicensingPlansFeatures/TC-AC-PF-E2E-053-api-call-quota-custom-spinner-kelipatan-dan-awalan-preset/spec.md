---
id: TC-AC-PF-E2E-053-api-call-quota-custom-spinner-kelipatan-dan-awalan-preset
title: "API Call Quota Custom: Spinner, Nilai Bukan Kelipatan, dan Awalan Nilai Preset"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PF-134
  - TC-AC-PF-135
  - TC-AC-PF-746
coverage:
  web: automated
---

# API Call Quota Custom: Spinner, Nilai Bukan Kelipatan, dan Awalan Nilai Preset

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Principal), akun #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.AC_TC_PASSWORD`); halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_ac-plans-features` true dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): sesi API aktor dan fixture backend idempoten untuk memulihkan Dataset Pre-setup dan menghapus plan buatan spec. General Settings (Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC) disiapkan fixture sebagai precondition TC dan tidak diubah spec.
- Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12): nilai Pre-setup dirujuk lewat kunci fixture yang dibuat tim FE; password dan token tidak ditulis di spec.
- Data Pre-setup: Dataset Plan A dengan default plan `Growth` (Open API ON).
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup (`Growth`) dipakai apa adanya, hanya dibaca (Template); pemulihan Dataset dijamin fixture backend idempoten yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini.
- Data Dinamis: Plan Name bersuffix `-{runId}-053`: `Paket Quota Tengah-{runId}-053` (API call quota 150000) dan `Paket Kuota Sepuluh Juta-{runId}-053` (API call quota 10000000).
- State global: Dataset Pre-setup bersama; suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Pembersihan: hook `after` menghapus plan buatan spec ini (nama bersuffix `-{runId}-053`) lewat fixture backend, memulihkan Dataset, dan mengembalikan sesi ke akun default suite.

## Test Steps

### Spinner increment dan decrement (TC-AC-PF-134)

1. Buka tab `Custom`, sub-tab `Active`
2. Klik `+ Custom Plan` pada toolbar
3. Pilih Product `FAMS` dan Template `Growth`
4. Pilih API call quota `Custom` lalu isi `100000`
5. Verifikasi tombol decrement Disabled pada nilai `100000`
6. Klik decrement
7. Isi nilai `10000000`
8. Verifikasi tombol increment Disabled pada nilai `10000000`
9. Isi nilai `100000` lalu klik increment
10. Verifikasi nilai menjadi `200000` (step 100.000)

### Nilai bukan kelipatan step (TC-AC-PF-135)

11. Isi Plan Name `Paket Quota Tengah-{runId}-053`
12. Isi API call quota `Custom` dengan `150000`
13. Klik `[Submit]`
14. Verifikasi tidak ada pesan error
15. Verifikasi toast sukses: "Success, custom plan has been created."
16. Buka Tab Overview Plan Detail
17. Verifikasi Tab Overview baris API call quota menampilkan `150,000/month` (nilai yang diketik tersimpan, tidak dibulatkan)

### Awalan nilai preset (TC-AC-PF-746)

18. Klik breadcrumb sub-tab `Active`
19. Klik `+ Custom Plan` pada toolbar
20. Pilih Product `FAMS`, Template `Growth`, isi Plan Name `Paket Kuota Sepuluh Juta-{runId}-053`
21. Pilih API call quota `Custom`
22. Ketik `10000` satu digit demi satu
23. Ketik digit keenam `0`
24. Verifikasi dropdown API call quota tetap `Custom` dan input menampilkan `100000` (tidak berganti menjadi `100K/month`)
25. Ketik digit ketujuh `0`
26. Verifikasi dropdown API call quota tetap `Custom` dan input menampilkan `1000000` (tidak berganti menjadi `1M/month`)
27. Ketik digit kedelapan `0`
28. Verifikasi input berisi `10000000`
29. Klik `[Submit]`
30. Verifikasi toast sukses: "Success, custom plan has been created."
31. Buka Tab Overview Plan Detail `Paket Kuota Sepuluh Juta-{runId}-053`
32. Verifikasi Tab Overview baris API call quota menampilkan `10,000,000/month`

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 18.
- Langkah klik decrement pada nilai `100000` dan klik increment pada TC-AC-PF-134 mengikuti TC; Expected TC hanya mengasersi state Disabled dan hasil increment, sehingga hasil klik decrement tidak diasersi.
- Langkah penghubung: breadcrumb sub-tab `Active` untuk membuka form baru setelah plan tersimpan; spec berakhir pada Plan Detail tanpa form dirty. Form dari TC-AC-PF-134 dilanjutkan oleh TC-AC-PF-135 (Product dan Template sudah terpilih, nilai Custom diganti).

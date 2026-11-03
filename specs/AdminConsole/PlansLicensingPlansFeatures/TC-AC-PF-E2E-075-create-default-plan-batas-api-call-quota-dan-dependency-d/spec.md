---
id: TC-AC-PF-E2E-075-create-default-plan-batas-api-call-quota-dan-dependency-d
title: "Create Default Plan: Batas Custom API Call Quota dan Dependency D-2 dan D-4"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-753
  - TC-AC-PF-754
coverage:
  web: automated
---

# Create Default Plan: Batas Custom API Call Quota dan Dependency D-2 dan D-4

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Andi Wijaya`; Global Role Manage plans & licensing Create, Read, Update, Delete), password dari `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman Plans & Licensing > Plans & Features (Default > Active) dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (nilai awal akun aktor); spec ini tidak mengubahnya.
- Data Pre-setup: Dataset Plan S (Default SAMS: `Supply Starter` Free dan `Supply Pro` Paid; slot Paid tersisa; payload fitur FAMS sebagai placeholder).
- Data Dinamis: `Supply Kuota Batas {runId}-075` (default plan Paid SAMS dengan API call quota Custom `10000000`, dibuat pada TC-AC-PF-753; dihapus fixture BE di hook `after`). Nilai Custom API call quota yang diketik: `99999`, `10000001`, `10000000`.
- Kemampuan teknis: fixture BE untuk menyemai dan memulihkan Dataset Pre-setup (idempoten, disediakan tim FE/BE). Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data dirujuk sebagai `Fixture.plansFeatures.<kunci>` dan ditandai di sini sebagai fixture yang belum ada.
- Pengecualian S-06/S-12 butir A-14: Dataset Pre-setup berslot terbatas (1 Free dan 3 Paid per Product) dan nama literal yang menentukan asersi dipakai tanpa suffix; pemulihan Dataset ke keadaan awal oleh fixture BE dijalankan di hook `before` dan `after` serta sebagai langkah penghubung yang tertulis pada Test Steps; data yang dibuat spec ini bersuffix `{runId}-075`.
- State global: Dataset Pre-setup bersama dipulihkan sebagaimana di atas dan suite berjalan serial (`parallel: false`, lihat `suite.md`). Tiap plan yang dibuat spec ini menambah entri Changelog permanen dan mengubah Last Updated tabel List; entri tidak dapat dihapus lewat UI dan tidak diasersi spec ini.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): fixture BE menghapus plan yang dibuat spec dan memulihkan Dataset.

## Test Steps

### TC-AC-PF-753: Create Default Plan: batas Custom API call quota 100.000 sampai 10.000.000 ditolak di luar rentang dan diterima di batas atas

1. Klik `+ Default Plan`
2. Pilih Product `SAMS`, Pricing Type `Paid`, dan isi Plan Name `Supply Kuota Batas {runId}-075`
3. Nyalakan Open API, pilih API call quota `Custom`, isi `99999`, klik `[Submit]`
4. Verifikasi pesan `Value must be between 100,000 and 10,000,000 calls/month` untuk nilai `99999`
5. Verifikasi form tetap terbuka
6. Klik `[Clear Field]`
7. Pilih Product `SAMS`, Pricing Type `Paid`, dan isi Plan Name `Supply Kuota Batas {runId}-075`
8. Nyalakan Open API, pilih API call quota `Custom`, isi `10000001`, klik `[Submit]`
9. Verifikasi pesan `Value must be between 100,000 and 10,000,000 calls/month` untuk nilai `10000001`
10. Verifikasi form tetap terbuka
11. Klik `[Clear Field]`
12. Pilih Product `SAMS`, Pricing Type `Paid`, dan isi Plan Name `Supply Kuota Batas {runId}-075`
13. Nyalakan Open API, pilih API call quota `Custom`, isi `10000000`, klik `[Submit]`
14. Verifikasi toast sukses: "Success, default plan has been created."
15. Buka Tab Overview Plan Detail `Supply Kuota Batas {runId}-075`
16. Verifikasi Tab Overview baris API call quota menampilkan `10,000,000/month`

### TC-AC-PF-754: Create Default Plan: dependency D-2 dan D-4 kedua arah menyesuaikan Group count, Group hierarchy depth, dan License allocation per group dengan inline warning

17. Klik breadcrumb sub-tab `Active`
18. Klik `+ Default Plan`
19. Pilih Product `SAMS` dan Pricing Type `Paid`
20. Ubah Group count menjadi `25`, Group hierarchy depth menjadi `5`, dan nyalakan License allocation per group
21. Ubah Group count menjadi `1`
22. Verifikasi Group hierarchy depth otomatis `1`
23. Verifikasi License allocation per group otomatis OFF
24. Verifikasi inline warning "Group hierarchy depth was changed automatically because group count requires it."
25. Verifikasi inline warning "License allocation per group was changed automatically because group count requires it."
26. Ubah Group hierarchy depth menjadi `2`
27. Verifikasi Group count otomatis `3`
28. Verifikasi Group hierarchy depth tetap `2`
29. Verifikasi inline warning "Group count was changed automatically because group hierarchy depth requires it."
30. Ubah Group count menjadi `1`, lalu nyalakan License allocation per group
31. Verifikasi Group count otomatis `3`
32. Verifikasi License allocation per group tetap ON
33. Verifikasi inline warning "Group count was changed automatically because license allocation per group requires it."
34. Klik `[Clear Field]`

## Notes

- Langkah penghubung (S-03, S-09, R-12): `[Clear Field]` pada langkah 6 dan 11 menghapus pesan error identik `Value must be between 100,000 and 10,000,000 calls/month` sebelum nilai berikutnya diuji sehingga asersi pesan tidak lulus karena sisa error; Product, Pricing Type, Plan Name, dan Custom API call quota diisi ulang sesudahnya. TC menulis "Ubah nilai menjadi ..." pada form yang sama; pengisian ulang setelah `[Clear Field]` menghasilkan state yang sama dengan pembersih di antara dua error identik. Langkah 17 kembali ke list dari Plan Detail dan langkah 34 mengosongkan form di akhir (S-09).
- Blok TC-AC-PF-754 (tanpa penulisan data) tidak dapat mendahului blok TC-AC-PF-753 karena blok TC-AC-PF-753 diakhiri dengan Plan Detail yang menyimpan plan; urutan validasi diblokir sebelum aksi sukses berlaku di dalam blok TC-AC-PF-753.
- Urutan langkah 20 sampai 34 mengikuti urutan state: perubahan Group count `25` ke `1`, depth `2`, lalu Group count `1` dengan License allocation per group ON, sesuai Langkah 2 sampai 5 TC-AC-PF-754.
- Temuan untuk QA:
-   - Post Condition TC yang tidak punya langkah observasi di TC (mis. `Tidak ada perubahan data`, `Default plan ... tersimpan`) tidak diasersi.
-   - TC-AC-PF-754 tidak menyebut pilihan API call quota atau nilai fitur lain; spec hanya mengubah field yang disebut TC.

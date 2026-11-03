---
id: TC-AC-PF-E2E-068-asset-cap-create-default-plan-kondisi-muncul-dan-validasi
title: "Asset Cap Create Default Plan: Kondisi Muncul dan Validasi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-177
  - TC-AC-PF-178
  - TC-AC-PF-179
  - TC-AC-PF-180
  - TC-AC-PF-181
coverage:
  web: automated
---

# Asset Cap Create Default Plan: Kondisi Muncul dan Validasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Andi Wijaya`; Global Role Manage plans & licensing Create, Read, Update, Delete), password dari `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman Plans & Licensing > Plans & Features (Default > Active) dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (nilai awal akun aktor); spec ini tidak mengubahnya.
- Data Pre-setup: Dataset Plan V2 (Default FAMS dengan 2 Paid aktif `Growth` dan `Professional`; Free `Starter` sudah di-archive), Dataset Plan U (SIEM dengan 1 Paid aktif `SIEM`, tanpa Free), Dataset Plan T (SAMS dengan 3 Paid aktif, tanpa Free), dan Dataset Plan V (Default FAMS dengan 3 Paid aktif `Growth`, `Professional`, `Enterprise`; Free `Starter` sudah di-archive). `before` menyemai Dataset Plan V2, U, dan T; langkah penghubung (langkah 12) memulihkan FAMS ke Dataset Plan V sebelum blok TC-AC-PF-179.
- Data Dinamis: `Paket Cap Uji {runId}-068` (Plan Name pada TC-AC-PF-179 sampai TC-AC-PF-181; selalu ditolak validasi sehingga tidak tersimpan). Nilai Asset cap yang diketik: kosong, `-1`, `2.5`.
- Kemampuan teknis: fixture BE untuk menyemai dan memulihkan Dataset Pre-setup (idempoten, disediakan tim FE/BE). Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data dirujuk sebagai `Fixture.plansFeatures.<kunci>` dan ditandai di sini sebagai fixture yang belum ada.
- Pengecualian S-06/S-12 butir A-14: Dataset Pre-setup berslot terbatas (1 Free dan 3 Paid per Product) dan nama literal yang menentukan asersi dipakai tanpa suffix; pemulihan Dataset ke keadaan awal oleh fixture BE dijalankan di hook `before` dan `after` serta sebagai langkah penghubung yang tertulis pada Test Steps; data yang dibuat spec ini bersuffix `{runId}-068`.
- State global: Dataset Pre-setup bersama dipulihkan sebagaimana di atas dan suite berjalan serial (`parallel: false`, lihat `suite.md`). Tiap plan yang dibuat spec ini menambah entri Changelog permanen dan mengubah Last Updated tabel List; entri tidak dapat dihapus lewat UI dan tidak diasersi spec ini.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): fixture BE menghapus plan yang dibuat spec dan memulihkan Dataset.

## Test Steps

### TC-AC-PF-177: Field Asset cap muncul untuk Product FAMS dengan Pricing Type Free dengan nilai awal 25 dan tidak muncul untuk Paid

1. Klik `+ Default Plan`
2. Pilih Product `FAMS`
3. Pilih Pricing Type `Free`
4. Verifikasi SectionCard Capacity Toggles: field `Asset cap` muncul sebagai number input dengan nilai awal `25`
5. Pilih Pricing Type `Paid`
6. Verifikasi SectionCard Capacity Toggles: field `Asset cap` tidak ada di form

### TC-AC-PF-178: Asset cap tidak muncul untuk Product SAMS dan SIEM walau Pricing Type Free

7. Pilih Product `SIEM`, Pricing Type `Free`
8. Verifikasi SectionCard Capacity Toggles Product SIEM: field `Asset cap` tidak ada
9. Ganti Product ke `SAMS`
10. Verifikasi SectionCard Capacity Toggles Product SAMS: field `Asset cap` tidak ada
11. Klik `[Clear Field]`
12. Pulihkan Product FAMS ke Dataset Plan V lewat fixture BE, lalu klik segmen `Plans & Features` pada breadcrumb

### TC-AC-PF-179: Validasi Asset cap Create Default Plan: nilai kosong ditolak setelah Submit

13. Klik `+ Default Plan`
14. Pilih Product `FAMS`, Pricing Type `Free`, isi Plan Name `Paket Cap Uji {runId}-068`
15. Isi Asset cap dengan nilai kosong
16. Klik `[Submit]`
17. Verifikasi pesan inline `Value must be a whole number of 0 or more` setelah Submit
18. Verifikasi plan tidak tersimpan: form tetap terbuka pada halaman New Default Plan tanpa toast sukses

### TC-AC-PF-180: Validasi Asset cap Create Default Plan: nilai negatif -1 ditolak setelah Submit

19. Klik `[Clear Field]`
20. Pilih Product `FAMS`, Pricing Type `Free`, isi Plan Name `Paket Cap Uji {runId}-068`
21. Isi Asset cap dengan `-1`
22. Klik `[Submit]`
23. Verifikasi pesan inline `Value must be a whole number of 0 or more` setelah Submit
24. Verifikasi plan tidak tersimpan: form tetap terbuka pada halaman New Default Plan tanpa toast sukses

### TC-AC-PF-181: Validasi Asset cap Create Default Plan: nilai desimal 2.5 ditolak setelah Submit

25. Klik `[Clear Field]`
26. Pilih Product `FAMS`, Pricing Type `Free`, isi Plan Name `Paket Cap Uji {runId}-068`
27. Isi Asset cap dengan `2.5`
28. Klik `[Submit]`
29. Verifikasi pesan inline `Value must be a whole number of 0 or more` setelah Submit
30. Verifikasi plan tidak tersimpan: form tetap terbuka pada halaman New Default Plan tanpa toast sukses
31. Klik `[Clear Field]`

## Notes

- Langkah penghubung (S-03, S-09, R-12): `[Clear Field]` pada langkah 19 dan 25 menghapus pesan error identik `Value must be a whole number of 0 or more` sebelum kasus berikutnya sehingga asersi pesan tidak lulus karena sisa error kasus sebelumnya; blok TC-AC-PF-180 dan TC-AC-PF-181 mengisi ulang Product, Pricing Type, dan Plan Name sesudahnya. Langkah 12 memulihkan data FAMS lewat fixture BE (A-6) dan membuka ulang halaman lewat breadcrumb pada form bersih; `[Clear Field]` pada langkah 11 mengosongkan form sebelum pemulihan itu.
- Form ditutup dalam keadaan error tanpa isi tersimpan di akhir spec; hook `after` tidak membuang form di browser, sehingga langkah 31 mengosongkan form (S-09).
- Pada TC-AC-PF-178, asersi absence `Asset cap` di Product SIEM dan SAMS memakai SectionCard Capacity Toggles yang tampil sebagai anchor permukaan (bagian 8b butir 2).
- Asersi "tidak ada plan baru" dan "plan tidak tersimpan" pada penolakan validasi ditulis sebagai form tetap terbuka pada halaman New Default Plan tanpa toast sukses; TC tidak memberi cara observasi lain.
- Temuan untuk QA:
-   - Post Condition TC yang tidak punya langkah observasi di TC (mis. `Tidak ada perubahan data`, `Default plan ... tersimpan`) tidak diasersi.
-   - TC-AC-PF-178 Langkah 3 hanya menyebut "Ganti Product ke SAMS" tanpa menyatakan apakah Pricing Type `Free` tetap terpilih setelah Product diganti; spec mengikuti teks TC.

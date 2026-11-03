---
id: TC-AC-PF-E2E-076-submit-sukses-create-default-plan-free-nama-trim-dan-nama-sama
title: "Submit Sukses Create Default Plan: Free FAMS, Nama Ter-trim, dan Nama Sama Lintas Product"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-172
  - TC-AC-PF-184
  - TC-AC-PF-187
  - TC-AC-PF-613
coverage:
  web: automated
---

# Submit Sukses Create Default Plan: Free FAMS, Nama Ter-trim, dan Nama Sama Lintas Product

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Andi Wijaya`; Global Role Manage plans & licensing Create, Read, Update, Delete), password dari `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman Plans & Licensing > Plans & Features (Default > Active) dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (nilai awal akun aktor); spec ini tidak mengubahnya.
- Data Pre-setup: Dataset Plan V (Default FAMS dengan 3 Paid aktif `Growth`, `Professional`, `Enterprise`; Free `Starter` sudah di-archive) dan Dataset Plan S (Default SAMS: `Supply Starter` Free dan `Supply Pro` Paid; slot Paid tersisa). Product SAMS pada TC-AC-PF-172 memakai Dataset Plan S dengan FAMS `Growth` dari Dataset Plan V. Langkah penghubung (langkah 11) memulihkan FAMS ke Dataset Plan V (A-6).
- Data Dinamis (dibuat spec ini, dihapus fixture BE di hook `after`): `Starter Baru {runId}-076` (Free FAMS, TC-AC-PF-184), `Free Pengganti {runId}-076` (Free FAMS, TC-AC-PF-187), `Supply Trim {runId}-076` (Paid SAMS, TC-AC-PF-613; diketik dengan tiga spasi di awal dan tiga spasi di akhir), dan `Growth` (Paid SAMS, TC-AC-PF-172; nama literal tanpa suffix karena asersi bergantung pada nama yang sama dengan default plan FAMS `Growth` dari Pre-setup, A-6).
- Kemampuan teknis: fixture BE untuk menyemai dan memulihkan Dataset Pre-setup (idempoten, disediakan tim FE/BE). Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data dirujuk sebagai `Fixture.plansFeatures.<kunci>` dan ditandai di sini sebagai fixture yang belum ada.
- Pengecualian S-06/S-12 butir A-14: Dataset Pre-setup berslot terbatas (1 Free dan 3 Paid per Product) dan nama literal yang menentukan asersi dipakai tanpa suffix; pemulihan Dataset ke keadaan awal oleh fixture BE dijalankan di hook `before` dan `after` serta sebagai langkah penghubung yang tertulis pada Test Steps; data yang dibuat spec ini bersuffix `{runId}-076`.
- State global: Dataset Pre-setup bersama dipulihkan sebagaimana di atas dan suite berjalan serial (`parallel: false`, lihat `suite.md`). Tiap plan yang dibuat spec ini menambah entri Changelog permanen dan mengubah Last Updated tabel List; entri tidak dapat dihapus lewat UI dan tidak diasersi spec ini.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): fixture BE menghapus plan yang dibuat spec dan memulihkan Dataset.

## Test Steps

### TC-AC-PF-184: Submit Create Default Plan Free FAMS berhasil: tier 0 tanpa menggeser plan lain

1. Klik `+ Default Plan`
2. Pilih Product `FAMS`, isi Plan Name `Starter Baru {runId}-076`, pilih Pricing Type `Free`
3. Biarkan Asset cap `25` dan klik `[Submit]`
4. Verifikasi toast sukses: "Success, default plan has been created."
5. Verifikasi halaman Plans & Licensing > Plans & Features > Default > Active > Detail terbuka dengan judul `Starter Baru {runId}-076 – v1`
6. Verifikasi badge Type `Default`
7. Verifikasi badge Pricing Type `Free`
8. Verifikasi Tab Overview memuat Asset cap `25`
9. Klik breadcrumb sub-tab `Active`
10. Verifikasi list tab Default Active: `Starter Baru {runId}-076` berada paling atas Product FAMS diikuti `Growth`, `Professional`, `Enterprise` (tidak ada plan Paid yang bergeser)
11. Pulihkan FAMS ke Dataset Plan V lewat fixture BE (Free `Starter` kembali di-archive)

### TC-AC-PF-187: Create Default Plan Free baru diizinkan setelah plan Free di-archive dan tidak menggeser plan Paid

12. Klik `+ Default Plan`
13. Pilih Product `FAMS` dan Pricing Type `Free`
14. Verifikasi opsi `Free` tersedia di radio Pricing Type
15. Isi Plan Name `Free Pengganti {runId}-076` lalu klik `[Submit]`
16. Verifikasi toast sukses: "Success, default plan has been created."
17. Klik breadcrumb sub-tab `Active`
18. Verifikasi plan Paid `Growth`, `Professional`, `Enterprise` tetap pada urutan tier masing-masing

### TC-AC-PF-613: Plan Name Create Default Plan di-trim otomatis: spasi di awal dan akhir dibuang saat tersimpan

19. Klik `+ Default Plan`
20. Pilih Product `SAMS`, pilih Pricing Type `Paid`, isi Plan Name dengan 3 spasi di awal, `Supply Trim {runId}-076`, dan 3 spasi di akhir
21. Klik `[Submit]`
22. Verifikasi toast sukses: "Success, default plan has been created."
23. Verifikasi Plan Detail menampilkan judul `Supply Trim {runId}-076 – v1` tanpa spasi di ujung
24. Klik breadcrumb sub-tab `Active`
25. Verifikasi baris list menampilkan `Supply Trim {runId}-076` ter-trim

### TC-AC-PF-172: Plan Name Create Default Plan boleh sama dengan default plan Product lain dan dengan custom plan

26. Klik `+ Default Plan`
27. Pilih Product `SAMS`, Pricing Type `Paid`
28. Isi Plan Name `Growth` dan tunggu 1 detik
29. Verifikasi tidak ada pesan duplikat `Plan name already exists`
30. Klik `[Submit]`
31. Verifikasi toast sukses: "Success, default plan has been created."

## Notes

- Tidak ada blok validasi yang diblokir pada spec ini; seluruh blok adalah aksi sukses sehingga urutan mengikuti nomor TC dengan blok Free FAMS lebih dulu. Langkah 11 memulihkan data FAMS karena TC-AC-PF-187 mensyaratkan slot Free kosong sedangkan TC-AC-PF-184 sudah mengisinya (langkah penghubung, S-03, S-09).
- Pada TC-AC-PF-184 dan TC-AC-PF-613, nama dan judul memakai suffix `{runId}-076` (R-06); asersi urutan list pada TC-AC-PF-184 memakai nama bersuffix. Langkah 28 menunggu 1 detik (debounce validasi keunikan, kurang dari 30 detik) dan asersi absence pesan duplikat memakai Plan Name terisi dan Pricing Type terpilih sebagai anchor permukaan yang sama (bagian 8b butir 2).
- Temuan untuk QA:
-   - Post Condition TC yang tidak punya langkah observasi di TC (mis. `Tidak ada perubahan data`, `Default plan ... tersimpan`) tidak diasersi.
-   - TC-AC-PF-172 menyebut Dataset Plan A (default `Growth` pada FAMS, custom `Growth Tier`), sedangkan Dataset Plan A mendefinisikan SAMS kosong dan Dataset Plan S mendefinisikan SAMS berisi plan; spec memakai Dataset Plan S dan Dataset Plan V (FAMS `Growth` ada pada keduanya).
-   - TC-AC-PF-172 tidak menyebut cara membuktikan nama sama dengan custom plan; spec hanya mengasersi bahwa tidak ada pesan duplikat dan plan tersimpan.

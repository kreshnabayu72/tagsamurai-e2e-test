---
id: TC-AC-PF-E2E-071-submit-sukses-create-default-plan-tier-ceiling-template
title: "Submit Sukses Create Default Plan: Tier, Ceiling Paid, dan Template"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-185
  - TC-AC-PF-186
  - TC-AC-PF-188
  - TC-AC-PF-189
coverage:
  web: automated
---

# Submit Sukses Create Default Plan: Tier, Ceiling Paid, dan Template

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Andi Wijaya`; Global Role Manage plans & licensing Create, Read, Update, Delete), password dari `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman Plans & Licensing > Plans & Features (Default > Active) dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (nilai awal akun aktor); spec ini tidak mengubahnya.
- Data Pre-setup: Dataset Plan U (Default SIEM dengan 1 Paid aktif `SIEM`, tanpa Free) dan Dataset Plan V2 (Default FAMS dengan 2 Paid aktif `Growth` dan `Professional`; Free `Starter` sudah di-archive). `before` menyemai keduanya; langkah penghubung (langkah 6) memulihkan SIEM ke Dataset Plan U (A-6).
- Data Dinamis (default plan yang dibuat spec ini, dihapus fixture BE di hook `after`): `SIEM Dua Baru {runId}-071` (Paid SIEM, TC-AC-PF-189), `SIEM Dua {runId}-071` dan `SIEM Tiga {runId}-071` (Paid SIEM, TC-AC-PF-186), `Enterprise Baru {runId}-071` (Paid FAMS, TC-AC-PF-185 dan dipakai TC-AC-PF-188).
- Kemampuan teknis: fixture BE untuk menyemai dan memulihkan Dataset Pre-setup (idempoten, disediakan tim FE/BE). Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data dirujuk sebagai `Fixture.plansFeatures.<kunci>` dan ditandai di sini sebagai fixture yang belum ada.
- Pengecualian S-06/S-12 butir A-14: Dataset Pre-setup berslot terbatas (1 Free dan 3 Paid per Product) dan nama literal yang menentukan asersi dipakai tanpa suffix; pemulihan Dataset ke keadaan awal oleh fixture BE dijalankan di hook `before` dan `after` serta sebagai langkah penghubung yang tertulis pada Test Steps; data yang dibuat spec ini bersuffix `{runId}-071`.
- State global: Dataset Pre-setup bersama dipulihkan sebagaimana di atas dan suite berjalan serial (`parallel: false`, lihat `suite.md`). Tiap plan yang dibuat spec ini menambah entri Changelog permanen dan mengubah Last Updated tabel List; entri tidak dapat dihapus lewat UI dan tidak diasersi spec ini.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): fixture BE menghapus plan yang dibuat spec dan memulihkan Dataset.

## Test Steps

### TC-AC-PF-189: Create Default Plan SIEM Paid berhasil sama seperti Product lain

1. Klik `+ Default Plan`
2. Pilih Product `SIEM`, isi Plan Name `SIEM Dua Baru {runId}-071`, pilih Pricing Type `Paid`
3. Klik `[Submit]`
4. Verifikasi toast sukses: "Success, default plan has been created."
5. Verifikasi Plan Detail memuat judul `SIEM Dua Baru {runId}-071 – v1`
6. Pulihkan SIEM ke Dataset Plan U lewat fixture BE, lalu klik breadcrumb sub-tab `Active`

### TC-AC-PF-186: Ceiling Paid: Create ke-3 plan Paid lolos dan setelahnya opsi Paid hilang dari radio

7. Klik `+ Default Plan`
8. Pilih Product `SIEM`, isi Plan Name `SIEM Dua {runId}-071`, pilih Pricing Type `Paid`, lalu klik `[Submit]`
9. Verifikasi toast sukses pembuatan kedua: "Success, default plan has been created."
10. Klik breadcrumb sub-tab `Active`
11. Klik `+ Default Plan`
12. Pilih Product `SIEM`, isi Plan Name `SIEM Tiga {runId}-071`, pilih Pricing Type `Paid`, lalu klik `[Submit]`
13. Verifikasi toast sukses pembuatan ketiga (plan Paid ke-3 lolos): "Success, default plan has been created."
14. Klik breadcrumb sub-tab `Active`
15. Klik `+ Default Plan`
16. Pilih Product `SIEM`
17. Verifikasi opsi radio `Free` tampil
18. Verifikasi opsi radio `Paid` tidak ada untuk Product `SIEM`
19. Klik `[Clear Field]`

### TC-AC-PF-185: Submit Create Default Plan Paid FAMS ditambahkan di ujung tier tanpa menyisip

20. Pilih Product `FAMS`, isi Plan Name `Enterprise Baru {runId}-071`, pilih Pricing Type `Paid`
21. Verifikasi helper text Pricing Type: "This will be paid tier 3 of 3 (rank 3)."
22. Klik `[Submit]`
23. Verifikasi toast sukses: "Success, default plan has been created."
24. Klik breadcrumb sub-tab `Active`
25. Verifikasi list Default Active urutan FAMS: `Growth`, `Professional`, `Enterprise Baru {runId}-071` (tier terakhir) tanpa pergeseran plan lain

### TC-AC-PF-188: Create Default Plan tersedia sebagai Template di Custom Plan Builder untuk Product yang sama

26. Klik tab `Custom`
27. Klik `+ Custom Plan`
28. Pilih Product `FAMS`
29. Buka dropdown Template
30. Verifikasi opsi Template memuat `Growth`, `Professional`, `Enterprise Baru {runId}-071`
31. Tutup dropdown Template tanpa memilih opsi
32. Klik segmen `Plans & Features` pada breadcrumb
33. Verifikasi dialog `Unsaved Changes` tampil
34. Klik `[Leave]`

## Notes

- Langkah penghubung (S-03, S-09): langkah 6 memulihkan SIEM ke Dataset Plan U lewat fixture BE (A-6) karena TC-AC-PF-186 mensyaratkan SIEM dengan 1 Paid aktif sedangkan TC-AC-PF-189 sudah menambah satu plan Paid; `[Clear Field]` pada langkah 19 mengembalikan form bersih sebelum blok TC-AC-PF-185; klik breadcrumb sub-tab `Active` kembali ke list dari Plan Detail.
- Dependensi: TC-AC-PF-188 mensyaratkan default plan Paid `Enterprise Baru` dari TC-AC-PF-185; langkah TC-AC-PF-185 dijalankan pada spec ini tepat sebelum blok TC-AC-PF-188 (S-04). TC-AC-PF-184 dan TC-AC-PF-187 ada di spec 076.
- Menutup form dirty pada TC-AC-PF-188 ditulis deterministik: breadcrumb, `Verifikasi` dialog `Unsaved Changes`, klik `[Leave]` (S-08).
- Urutan blok berbeda dari urutan nomor TC supaya data Dataset Plan U sesuai precondition tiap TC: TC-AC-PF-189 mendahului TC-AC-PF-186 karena TC-AC-PF-186 menambah plan Paid hingga batas ceiling.
- Temuan untuk QA:
-   - Post Condition TC yang tidak punya langkah observasi di TC (mis. `Tidak ada perubahan data`, `Default plan ... tersimpan`) tidak diasersi.
-   - TC-AC-PF-186 menyebut pembuatan plan kedua dan ketiga dalam satu langkah tanpa menyatakan apakah halaman dibuka ulang di antaranya; spec membuka form baru lewat breadcrumb sub-tab `Active` dan `+ Default Plan` untuk tiap pembuatan.

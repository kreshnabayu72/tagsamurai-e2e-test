---
id: TC-AC-PF-E2E-067-pricing-type-create-default-plan-radio-tersaring-dan
title: "Pricing Type Create Default Plan: Radio Tersaring dan Helper Text"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-173
  - TC-AC-PF-174
  - TC-AC-PF-175
  - TC-AC-PF-176
coverage:
  web: automated
---

# Pricing Type Create Default Plan: Radio Tersaring dan Helper Text

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Andi Wijaya`; Global Role Manage plans & licensing Create, Read, Update, Delete), password dari `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman Plans & Licensing > Plans & Features (Default > Active) dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (nilai awal akun aktor); spec ini tidak mengubahnya.
- Data Pre-setup: Dataset Plan S (Default SAMS: `Supply Starter` Free dan `Supply Pro` Paid; slot Paid tersisa), Dataset Plan A (SIEM `SIEM` Paid; FAMS penuh), Dataset Plan U (SIEM dengan 1 Paid aktif `SIEM`, tanpa Free), dan Dataset Plan T (SAMS dengan 3 Paid aktif `Supply Tiga A`, `Supply Tiga B`, `Supply Tiga C`, tanpa Free). Dataset Plan S dan Dataset Plan T mendefinisikan Product SAMS secara berbeda: `before` menyemai Dataset Plan S dan Dataset Plan A (SIEM sama dengan Dataset Plan U), lalu langkah penghubung (langkah 12) memulihkan SAMS ke Dataset Plan T sebelum blok TC-AC-PF-175.
- Data Dinamis: `Paket Tanpa Tipe {runId}-067` (Plan Name yang diketik pada TC-AC-PF-173; ditolak validasi sehingga tidak tersimpan).
- Kemampuan teknis: fixture BE untuk menyemai dan memulihkan Dataset Pre-setup (idempoten, disediakan tim FE/BE). Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data dirujuk sebagai `Fixture.plansFeatures.<kunci>` dan ditandai di sini sebagai fixture yang belum ada.
- Pengecualian S-06/S-12 butir A-14: Dataset Pre-setup berslot terbatas (1 Free dan 3 Paid per Product) dan nama literal yang menentukan asersi dipakai tanpa suffix; pemulihan Dataset ke keadaan awal oleh fixture BE dijalankan di hook `before` dan `after` serta sebagai langkah penghubung yang tertulis pada Test Steps; data yang dibuat spec ini bersuffix `{runId}-067`.
- State global: Dataset Pre-setup bersama dipulihkan sebagaimana di atas dan suite berjalan serial (`parallel: false`, lihat `suite.md`). Tiap plan yang dibuat spec ini menambah entri Changelog permanen dan mengubah Last Updated tabel List; entri tidak dapat dihapus lewat UI dan tidak diasersi spec ini.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): fixture BE menghapus plan yang dibuat spec dan memulihkan Dataset.

## Test Steps

### TC-AC-PF-173: Pricing Type Create Default Plan wajib dipilih: Submit tanpa pilihan ditolak

1. Klik `+ Default Plan`
2. Pilih Product `SAMS`, isi Plan Name `Paket Tanpa Tipe {runId}-067`
3. Verifikasi tidak ada pilihan terpilih pada radio Pricing Type
4. Klik `[Submit]` tanpa memilih Pricing Type
5. Verifikasi pesan inline `Pricing type must not be empty`
6. Verifikasi plan tidak tersimpan: form tetap terbuka pada halaman New Default Plan tanpa toast sukses
7. Klik `[Clear Field]`

### TC-AC-PF-174: Opsi radio Pricing Type menyaring Free saat Product sudah punya plan Free

8. Pilih Product `SAMS`
9. Verifikasi opsi `Paid` tampil di radio Pricing Type
10. Verifikasi opsi `Free` tidak ada di radio Pricing Type (Invariant #1)
11. Klik `[Clear Field]`
12. Pulihkan Product SAMS ke Dataset Plan T lewat fixture BE, lalu klik segmen `Plans & Features` pada breadcrumb

### TC-AC-PF-175: Opsi radio Pricing Type menyaring Paid saat Product sudah mencapai tiga plan Paid

13. Klik `+ Default Plan`
14. Pilih Product `SAMS`
15. Verifikasi opsi `Free` tampil di radio Pricing Type
16. Verifikasi opsi `Paid` tidak ada di radio Pricing Type (Invariant #2)
17. Klik `[Clear Field]`

### TC-AC-PF-176: Helper text Pricing Type Free dan Paid live menyebut tier sesuai jumlah plan Paid aktif

18. Pilih Product `SIEM`
19. Pilih Pricing Type `Free`
20. Verifikasi helper text Free: "This will be the free plan for this product (rank 0)."
21. Pilih Pricing Type `Paid`
22. Verifikasi helper text Paid: "This will be paid tier 2 of 3 (rank 2)."
23. Klik `[Clear Field]`

## Notes

- Langkah penghubung (S-03, S-09): `[Clear Field]` di akhir tiap blok TC mengembalikan form ke keadaan bersih sehingga TC berikutnya tidak mewarisi pilihan dan form tidak berakhir dirty. Langkah 12 memulihkan data SAMS lewat fixture BE (A-6) dan membuka ulang halaman lewat breadcrumb pada form bersih (tanpa dialog Unsaved Changes) supaya dropdown Product dimuat dari data terbaru; langkah 13 membuka form lagi.
- Pada TC-AC-PF-174 dan TC-AC-PF-175 opsi yang tampil diasersi lebih dulu sebagai anchor positif sebelum asersi absence opsi lain pada radio yang sama (bagian 8b butir 2).
- Asersi "tidak ada plan baru" dan "plan tidak tersimpan" pada penolakan validasi ditulis sebagai form tetap terbuka pada halaman New Default Plan tanpa toast sukses; TC tidak memberi cara observasi lain.
- Temuan untuk QA:
-   - Post Condition TC yang tidak punya langkah observasi di TC (mis. `Tidak ada perubahan data`, `Default plan ... tersimpan`) tidak diasersi.
-   - TC-AC-PF-174 menyebut Dataset Plan A dan Dataset Plan S, sedangkan TC-AC-PF-175 menyebut Dataset Plan T; ketiganya mendefinisikan Product SAMS secara berbeda (S: 1 Free dan 1 Paid, T: 3 Paid, A: kosong). Spec memakai Dataset Plan S pada TC-AC-PF-173 dan TC-AC-PF-174, Dataset Plan T pada TC-AC-PF-175, dan SIEM Dataset Plan A/U pada TC-AC-PF-176 dengan pemulihan lewat fixture BE di langkah 12.

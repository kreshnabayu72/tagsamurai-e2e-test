---
id: TC-AC-PF-E2E-072-clear-field-dan-unsaved-changes-dasar-create-default-plan
title: "Clear Field dan Unsaved Changes Dasar pada Create Default Plan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-190
  - TC-AC-PF-191
  - TC-AC-PF-643
coverage:
  web: automated
---

# Clear Field dan Unsaved Changes Dasar pada Create Default Plan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Andi Wijaya`; Global Role Manage plans & licensing Create, Read, Update, Delete), password dari `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman Plans & Licensing > Plans & Features (Default > Active) dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (nilai awal akun aktor); spec ini tidak mengubahnya.
- Data Pre-setup: Dataset Plan V (Default FAMS dengan 3 Paid aktif `Growth`, `Professional`, `Enterprise`; Free `Starter` sudah di-archive; Product FAMS tersedia di dropdown karena slot Free kosong) dan Product SAMS tanpa plan (kondisi Dataset Plan A pada TC-AC-PF-643). Spec ini tidak membuat atau mengubah plan.
- Data Dinamis: nilai Plan Name yang diketik: `Paket Reset {runId}-072`, `Paket Dirty {runId}-072` (form tidak pernah disubmit sehingga tidak tersimpan).
- Kemampuan teknis: fixture BE untuk menyemai dan memulihkan Dataset Pre-setup (idempoten, disediakan tim FE/BE). Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data dirujuk sebagai `Fixture.plansFeatures.<kunci>` dan ditandai di sini sebagai fixture yang belum ada.
- Pengecualian S-06/S-12 butir A-14: Dataset Pre-setup berslot terbatas (1 Free dan 3 Paid per Product) dan nama literal yang menentukan asersi dipakai tanpa suffix; pemulihan Dataset ke keadaan awal oleh fixture BE dijalankan di hook `before` dan `after` serta sebagai langkah penghubung yang tertulis pada Test Steps; data yang dibuat spec ini bersuffix `{runId}-072`.
- State global: Dataset Pre-setup bersama dipulihkan sebagaimana di atas dan suite berjalan serial (`parallel: false`, lihat `suite.md`). Tiap plan yang dibuat spec ini menambah entri Changelog permanen dan mengubah Last Updated tabel List; entri tidak dapat dihapus lewat UI dan tidak diasersi spec ini.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): fixture BE menghapus plan yang dibuat spec dan memulihkan Dataset.

## Test Steps

### TC-AC-PF-643: Clear Field Create Default Plan menghapus pesan error inline dan memindahkan fokus ke field Product

1. Klik `+ Default Plan`
2. Klik `[Submit]` tanpa mengisi apa pun
3. Verifikasi pesan error `Product must not be empty`
4. Verifikasi pesan error `Plan name must not be empty`
5. Verifikasi pesan error `Pricing type must not be empty`
6. Klik `[Clear Field]`
7. Verifikasi seluruh pesan error hilang
8. Verifikasi border merah pada field hilang
9. Verifikasi fokus berada pada field Product
10. Verifikasi tidak ada dialog konfirmasi
11. Verifikasi form tetap terbuka

### TC-AC-PF-190: Clear Field Create Default Plan mengembalikan nilai awal form tanpa dialog

12. Pilih Product `FAMS`, Pricing Type `Free`, isi Plan Name `Paket Reset {runId}-072`, ubah Group count ke `25` dan Asset cap ke `99`
13. Klik `[Clear Field]`
14. Verifikasi Product kembali `Select product`
15. Verifikasi Plan Name kosong
16. Verifikasi tidak ada Pricing Type terpilih
17. Verifikasi Capacity kembali ke opsi terkecil
18. Verifikasi Binary Toggles kembali OFF
19. Verifikasi Feature Suites kembali `None`
20. Verifikasi tidak ada dialog konfirmasi
21. Klik `[Submit]`
22. Verifikasi pesan error Required `Product must not be empty`
23. Verifikasi pesan error Required `Plan name must not be empty`
24. Verifikasi pesan error Required `Pricing type must not be empty`

### TC-AC-PF-191: Form Create Default Plan dirty lalu klik breadcrumb: dialog Unsaved Changes dengan Cancel dan Leave

25. Klik `[Clear Field]`
26. Pilih Product `FAMS` dan isi Plan Name `Paket Dirty {runId}-072`
27. Klik segmen `Plans & Features` pada breadcrumb
28. Verifikasi dialog `Unsaved Changes` dengan body "You have unsaved changes. Are you sure you want to leave?"
29. Klik `[Cancel]`
30. Verifikasi dialog tertutup
31. Verifikasi user tetap di Plans & Licensing > Plans & Features > New Default Plan
32. Klik segmen `Plans & Features` pada breadcrumb lagi
33. Klik `[Leave]`
34. Verifikasi halaman Plans & Licensing > Plans & Features > Default > Active tampil

## Notes

- Langkah penghubung (S-03, S-09, R-12): `[Clear Field]` pada langkah 25 menghapus pesan error Required sisa TC-AC-PF-190 sebelum TC-AC-PF-191 dan mengembalikan form ke keadaan bersih. Blok TC-AC-PF-643 mendahului TC-AC-PF-190 karena TC-AC-PF-643 dimulai dari form yang belum pernah diisi; pesan error identik pada TC-AC-PF-643 dan TC-AC-PF-190 dipisah oleh `[Clear Field]` dan pengisian ulang.
- Blok TC-AC-PF-191 diakhiri dengan `[Leave]` sehingga form tidak berakhir dirty (S-08). TC-AC-PF-192 dan TC-AC-PF-664 ada di spec 077.
- Temuan untuk QA:
-   - Post Condition TC yang tidak punya langkah observasi di TC (mis. `Tidak ada perubahan data`, `Default plan ... tersimpan`) tidak diasersi.
-   - TC-AC-PF-191 Expected b menulis `[Leave]` "membuang perubahan" tanpa langkah observasi atas pembuangan itu; spec mengasersi halaman tujuan tampil (S-03, kesimpulan yang tidak teramati terpisah).
-   - TC-AC-PF-643 dan TC-AC-PF-191 menyebut Dataset Plan A, sedangkan TC-AC-PF-190 dan TC-AC-PF-191 menyebut Dataset Plan V; Product FAMS hanya muncul di dropdown pada Dataset Plan V (slot Free kosong), sehingga spec memakai Dataset Plan V untuk seluruh blok.

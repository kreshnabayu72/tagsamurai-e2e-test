---
id: TC-AC-PF-E2E-073-unsaved-changes-create-default-plan-sidebar-back-esc-auto
title: "Unsaved Changes, Auto-Focus, Enter, dan Esc pada Create Default Plan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-668
  - TC-AC-PF-671
  - TC-AC-PF-732
  - TC-AC-PF-737
  - TC-AC-PF-742
coverage:
  web: automated
---

# Unsaved Changes, Auto-Focus, Enter, dan Esc pada Create Default Plan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Andi Wijaya`; Global Role Manage plans & licensing Create, Read, Update, Delete), password dari `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman Plans & Licensing > Plans & Features (Default > Active) dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (nilai awal akun aktor); spec ini tidak mengubahnya.
- Data Pre-setup: Dataset Plan A (Default aktif FAMS penuh dengan Starter, Growth, Professional, Enterprise; SIEM `SIEM`; SAMS tanpa plan sehingga Product SAMS tersedia di dropdown). Spec ini tidak membuat atau mengubah plan.
- Data Dinamis: nilai Plan Name yang diketik: `Supply Enter {runId}-073` dan `Paket Dirty {runId}-073` (form tidak pernah tersimpan).
- Kemampuan teknis tambahan: menekan tombol Back browser, Esc, dan Enter pada form.
- Kemampuan teknis: fixture BE untuk menyemai dan memulihkan Dataset Pre-setup (idempoten, disediakan tim FE/BE). Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data dirujuk sebagai `Fixture.plansFeatures.<kunci>` dan ditandai di sini sebagai fixture yang belum ada.
- Pengecualian S-06/S-12 butir A-14: Dataset Pre-setup berslot terbatas (1 Free dan 3 Paid per Product) dan nama literal yang menentukan asersi dipakai tanpa suffix; pemulihan Dataset ke keadaan awal oleh fixture BE dijalankan di hook `before` dan `after` serta sebagai langkah penghubung yang tertulis pada Test Steps; data yang dibuat spec ini bersuffix `{runId}-073`.
- State global: Dataset Pre-setup bersama dipulihkan sebagaimana di atas dan suite berjalan serial (`parallel: false`, lihat `suite.md`). Tiap plan yang dibuat spec ini menambah entri Changelog permanen dan mengubah Last Updated tabel List; entri tidak dapat dihapus lewat UI dan tidak diasersi spec ini.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): fixture BE menghapus plan yang dibuat spec dan memulihkan Dataset.

## Test Steps

### TC-AC-PF-732: Create Default Plan: input pertama langsung ter-focus saat form muncul dan Enter tidak men-submit

1. Klik `+ Default Plan`
2. Verifikasi saat form muncul fokus langsung berada di field Product
3. Pilih Product `SAMS`, Pricing Type `Free`, dan isi Plan Name `Supply Enter {runId}-073`
4. Tekan Enter saat fokus berada di field Plan Name
5. Verifikasi Enter tidak men-submit: tidak ada toast
6. Verifikasi form tetap terbuka dengan input dipertahankan

### TC-AC-PF-737: Create Default Plan dirty lalu tekan Esc: dialog Unsaved Changes muncul

7. Tekan Esc
8. Verifikasi dialog `Unsaved Changes` dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
9. Klik `[Cancel]` pada dialog
10. Verifikasi user tetap di form
11. Verifikasi input dipertahankan
12. Klik `[Clear Field]`

### TC-AC-PF-742: Create Default Plan bersih lalu tekan Esc: kembali ke daftar tanpa dialog

13. Tekan Esc tanpa mengubah apa pun
14. Verifikasi halaman Plans & Licensing > Plans & Features > Default > Active tampil langsung
15. Verifikasi tidak ada dialog `Unsaved Changes`

### TC-AC-PF-668: Form Create Default Plan dirty lalu klik menu sidebar: dialog Unsaved Changes dengan Cancel dan Leave

16. Klik `+ Default Plan` pada tab Default sub-tab Active
17. Pilih Product `SAMS` dan isi Plan Name `Paket Dirty {runId}-073`
18. Klik menu Plans & Licensing > Plans & Features di sidebar
19. Verifikasi dialog `Unsaved Changes` dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
20. Verifikasi halaman belum berpindah
21. Klik `[Cancel]` pada dialog
22. Verifikasi dialog tertutup
23. Verifikasi user tetap di form dengan input dipertahankan
24. Klik menu Plans & Licensing > Plans & Features di sidebar lagi
25. Klik `[Leave]`
26. Verifikasi navigasi dilanjutkan: halaman Plans & Licensing > Plans & Features tampil

### TC-AC-PF-671: Form Create Default Plan dirty lalu tombol Back browser: dialog Unsaved Changes muncul

27. Klik `+ Default Plan` pada tab Default sub-tab Active
28. Pilih Product `SAMS` dan isi Plan Name `Paket Dirty {runId}-073`
29. Klik tombol Back browser
30. Verifikasi dialog `Unsaved Changes` dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
31. Klik `[Cancel]` pada dialog
32. Verifikasi user tetap di form dengan input dipertahankan
33. Klik `[Clear Field]`

## Notes

- Langkah penghubung (S-03, S-09): `[Clear Field]` pada langkah 12 dan langkah 33 mengembalikan form dirty ke keadaan bersih (tidak berakhir dirty). Blok TC-AC-PF-737 memakai kembali form yang sudah terisi pada blok TC-AC-PF-732 karena nilai input identik (Product `SAMS`, Pricing Type `Free`, Plan Name sama); halaman yang sama dipakai berulang tanpa submit (bagian 3 prinsip 13).
- Blok TC-AC-PF-732 ditempatkan pertama karena asersi fokus awal hanya bermakna pada form yang baru dibuka (bagian 8b butir 5).
- Pada blok TC-AC-PF-742 tampilnya halaman Default > Active diasersi lebih dulu sebagai anchor positif sebelum asersi absence dialog (bagian 8b butir 2).
- Temuan untuk QA:
-   - Post Condition TC yang tidak punya langkah observasi di TC (mis. `Tidak ada perubahan data`, `Default plan ... tersimpan`) tidak diasersi.
-   - TC-AC-PF-732 Expected b menulis "tidak ada perubahan data" tanpa cara observasi; spec mengasersi tidak ada toast dan form tetap terbuka dengan input dipertahankan.
-   - TC-AC-PF-668 Expected c menulis "tidak ada plan baru dan nilai plan tidak berubah" tanpa langkah observasi di list; spec mengasersi navigasi dilanjutkan saja.

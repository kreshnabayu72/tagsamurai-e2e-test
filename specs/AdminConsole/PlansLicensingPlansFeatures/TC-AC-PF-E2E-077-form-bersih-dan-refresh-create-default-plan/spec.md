---
id: TC-AC-PF-E2E-077-form-bersih-dan-refresh-create-default-plan
title: "Form Create Default Plan Bersih Tanpa Dialog dan Refresh F5 saat Dirty"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-192
  - TC-AC-PF-664
coverage:
  web: automated
---

# Form Create Default Plan Bersih Tanpa Dialog dan Refresh F5 saat Dirty

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Andi Wijaya`; Global Role Manage plans & licensing Create, Read, Update, Delete), password dari `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman Plans & Licensing > Plans & Features (Default > Active) dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (nilai awal akun aktor); spec ini tidak mengubahnya.
- Data Pre-setup: Dataset Plan V (Default FAMS dengan 3 Paid aktif; Free `Starter` sudah di-archive) dan Product SAMS tanpa plan (kondisi Dataset Plan A pada TC-AC-PF-664). Spec ini tidak membuat atau mengubah plan.
- Data Dinamis: nilai Plan Name yang diketik: `a` (lalu dihapus) dan `Paket Dirty {runId}-077` (form tidak pernah disubmit).
- Kemampuan teknis tambahan: menekan F5 dan menangani dialog bawaan browser `beforeunload` (mengamati kemunculannya lalu membatalkan muat ulang).
- Kemampuan teknis: fixture BE untuk menyemai dan memulihkan Dataset Pre-setup (idempoten, disediakan tim FE/BE). Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data dirujuk sebagai `Fixture.plansFeatures.<kunci>` dan ditandai di sini sebagai fixture yang belum ada.
- Pengecualian S-06/S-12 butir A-14: Dataset Pre-setup berslot terbatas (1 Free dan 3 Paid per Product) dan nama literal yang menentukan asersi dipakai tanpa suffix; pemulihan Dataset ke keadaan awal oleh fixture BE dijalankan di hook `before` dan `after` serta sebagai langkah penghubung yang tertulis pada Test Steps; data yang dibuat spec ini bersuffix `{runId}-077`.
- State global: Dataset Pre-setup bersama dipulihkan sebagaimana di atas dan suite berjalan serial (`parallel: false`, lihat `suite.md`). Tiap plan yang dibuat spec ini menambah entri Changelog permanen dan mengubah Last Updated tabel List; entri tidak dapat dihapus lewat UI dan tidak diasersi spec ini.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): fixture BE menghapus plan yang dibuat spec dan memulihkan Dataset.

## Test Steps

### TC-AC-PF-192: Form Create Default Plan bersih atau dikembalikan identik tidak memunculkan dialog Unsaved Changes

1. Klik `+ Default Plan`
2. Klik segmen `Plans & Features` pada breadcrumb tanpa mengisi apa pun
3. Verifikasi halaman Plans & Licensing > Plans & Features > Default > Active tampil langsung pada percobaan pertama
4. Verifikasi tidak ada dialog `Unsaved Changes` pada percobaan pertama
5. Klik `+ Default Plan`
6. Ketik `a` pada Plan Name lalu hapus kembali sehingga kosong
7. Klik segmen `Plans & Features` pada breadcrumb
8. Verifikasi halaman Plans & Licensing > Plans & Features > Default > Active tampil langsung pada percobaan kedua
9. Verifikasi tidak ada dialog `Unsaved Changes` pada percobaan kedua

### TC-AC-PF-664: Form Create Default Plan dirty lalu refresh F5: konfirmasi bawaan browser muncul

10. Klik `+ Default Plan` pada tab Default sub-tab Active
11. Pilih Product `SAMS` dan isi Plan Name `Paket Dirty {runId}-077`
12. Tekan F5
13. Verifikasi konfirmasi bawaan browser (`beforeunload`) muncul karena form dirty
14. Batalkan muat ulang pada dialog bawaan browser sehingga tetap di halaman
15. Klik `[Clear Field]`

## Notes

- Langkah penghubung (S-03, S-08, S-09): pembatalan muat ulang dan `[Clear Field]` pada langkah 14 dan 15 membuat form tidak berakhir dirty; kemampuan menangani dialog `beforeunload` tertulis di Prerequisites. TC-AC-PF-664 tidak mengasersi teks dialog karena ditentukan browser.
- Pada TC-AC-PF-192 halaman tujuan tampil diasersi lebih dulu sebagai anchor positif sebelum asersi absence dialog (bagian 8b butir 2).
- Temuan untuk QA:
-   - Post Condition TC yang tidak punya langkah observasi di TC (mis. `Tidak ada perubahan data`, `Default plan ... tersimpan`) tidak diasersi.
-   - TC-AC-PF-664 tidak menyebut pilihan pada dialog `beforeunload` (batal atau lanjut muat ulang); spec membatalkan muat ulang agar form tetap dapat dibersihkan.

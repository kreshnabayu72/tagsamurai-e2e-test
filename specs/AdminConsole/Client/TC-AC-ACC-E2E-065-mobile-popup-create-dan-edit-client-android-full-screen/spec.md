---
id: TC-AC-ACC-E2E-065-mobile-popup-create-dan-edit-client-android-full-screen
title: "Mobile Android: Form New Client dan Edit Client Full-Screen Satu Kolom dengan Footer Sticky"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-888
  - TC-AC-ACC-889
coverage:
  mobile: automated
---

# Mobile Android: Form New Client dan Edit Client Full-Screen Satu Kolom dengan Footer Sticky

## Prerequisites

- Mode: FE+BE. Platform: aplikasi native Android (PRD client §4.6 Mobile Layout); tampilan berupa card list dan form full-screen.
- Perangkat atau emulator Android dengan aplikasi native TAG Samurai Admin Console terpasang, serta kemampuan mengetuk elemen UI dan men-scroll body form (`parallel: false` untuk perangkat fisik bersama).
- Akun aktor: Total Control Principal (A-01) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`; Active-Full (A-15) `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login akun Total Control Principal di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Dataset seed: Client `PT Sejahtera Abadi {runId}-065` (setara C-01: Active, Default User Activated). Seeding Client lewat API/fixture BE di hook `before` (kemampuan disediakan tim FE/BE; endpoint tidak dikarang).
- Cleanup: hook `after` menghapus lewat API (soft-delete) Client yang dibuat atau di-seed spec ini, tanpa mengasumsikan setup berhasil penuh.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

### TC-888: Form New Client (Total Control)

1. Ketuk `[+ New Client]` di bawah toolbar
2. Verifikasi form "New Client" tampil full-screen (bukan popup lebar 600px)
3. Scroll body form dari Section "Company Information" sampai Section "Default User"
4. Verifikasi field tersusun satu kolom vertikal: Section "Company Information", "PIC", "Address", "Partner & Group", dan "Default User" berurutan
5. Verifikasi First Name dan Last Name tidak berdampingan
6. Verifikasi footer tetap terlihat di bawah layar saat body di-scroll (sticky)
7. Verifikasi footer memuat checkbox "Stay on this form after submitting", `[Clear Field]`, dan `[Submit]`
8. Tutup form tanpa menyimpan

### TC-889: Form Edit Client (Active-Full)

9. `Logout`, lalu login sebagai Active-Full (A-15)
10. Ketik Search `PT Sejahtera Abadi {runId}-065`, tekan Enter
11. Ketuk `⋯` pada card "PT Sejahtera Abadi {runId}-065" lalu pilih `Edit` di bottom sheet
12. Verifikasi form "Edit Client" tampil full-screen (bukan popup) dengan field terisi nilai saat ini
13. Scroll body form dari atas sampai bawah
14. Verifikasi field tersusun satu kolom vertikal tanpa pasangan field berdampingan
15. Verifikasi footer tetap terlihat di bawah layar saat body di-scroll (sticky)
16. Verifikasi footer memuat tombol `[Save]`
17. Tutup form tanpa menyimpan

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Ganti akun eksplisit (Total Control ke Active-Full) pada TC-889; bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal.
- Langkah penghubung (S-03): "Tutup form tanpa menyimpan" (form belum diubah, tanpa dialog) dan Search nama unik pada card list.
- Temuan untuk QA:
  - TC-888 dan TC-889 bertanda Manual Only (aplikasi native Android); cara menutup form full-screen di Android tidak disebut TC.

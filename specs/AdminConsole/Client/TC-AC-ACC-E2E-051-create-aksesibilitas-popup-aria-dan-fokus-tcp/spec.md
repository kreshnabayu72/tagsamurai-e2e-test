---
id: TC-AC-ACC-E2E-051-create-aksesibilitas-popup-aria-dan-fokus-tcp
title: "Aksesibilitas Popup New Client: aria-required, aria-describedby, dan Fokus Terkunci (Total Control)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-750
  - TC-AC-ACC-751
  - TC-AC-ACC-752
coverage:
  web: automated
---

# Aksesibilitas Popup New Client: aria-required, aria-describedby, dan Fokus Terkunci (Total Control)

## Prerequisites

- Mode: FE+BE. Tidak ada data yang dibuat.
- Akun aktor: Total Control Principal (A-01) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login akun Total Control Principal di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Tabel Field wajib (TC-750; popup Create oleh Total Control, Client Direct): Company Name, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Select Group, First Name, Last Name, Email, Division.
- Tabel Field teks wajib (TC-751): Company Name, PIC Name, PIC Email, Address, Postal Code, First Name, Last Name, Email, Division.
- Kemampuan teknis: membaca atribut `aria-required` dan `aria-describedby` elemen field, serta menekan Tab, Shift+Tab, dan Esc.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

1. Klik `[+ New Client]`

### TC-750: aria-required

2. Untuk setiap field pada tabel Field wajib, lakukan langkah 3
3. Verifikasi atribut `aria-required` field bernilai "true"

### TC-751: aria-describedby pada field error

4. Klik `[Submit]` dengan seluruh field kosong
5. Untuk setiap field pada tabel Field teks wajib, lakukan langkah 6 sampai 7
6. Verifikasi pesan error inline tampil di bawah field
7. Verifikasi `aria-describedby` field menunjuk ke elemen pesan error milik field tersebut

### TC-752: Fokus terkunci di dalam popup

8. Tekan Tab berulang kali hingga fokus mencapai tombol `[Submit]`
9. Verifikasi fokus hanya berpindah di antara kontrol di dalam popup dan tidak pernah berpindah ke halaman List di belakang popup
10. Tekan Tab satu kali lagi
11. Verifikasi fokus menuju kontrol fokus pertama di dalam popup
12. Tekan Shift+Tab pada kontrol fokus pertama di dalam popup
13. Verifikasi fokus menuju kontrol fokus terakhir di dalam popup (tombol `[Submit]`)
14. Tekan Esc
15. Verifikasi popup tertutup langsung
16. Verifikasi dialog Unsaved Changes tidak muncul (form belum diubah)

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Langkah 3 diulang untuk 13 field dan langkah 6 sampai 7 untuk 9 field (butir 8b-7).
- Form tetap belum diubah setelah `[Submit]` dengan seluruh field kosong, sehingga Esc pada TC-752 menutup popup tanpa dialog.
- Temuan untuk QA:
  - TC-750 menyebut field Select Group dengan `aria-required`, sedangkan TC-751 tidak menyertakan Select Group pada pemeriksaan aria-describedby; spec mengikuti anggota masing-masing TC.

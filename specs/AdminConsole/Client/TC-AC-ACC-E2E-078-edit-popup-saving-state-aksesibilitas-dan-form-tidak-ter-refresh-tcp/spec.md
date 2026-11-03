---
id: TC-AC-ACC-E2E-078-edit-popup-saving-state-aksesibilitas-dan-form-tidak-ter-refresh-tcp
title: "Popup Edit Client: Saving State, Aksesibilitas, dan Form Tidak Ter-Refresh oleh Perubahan Sesi Lain (Total Control)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-753
  - TC-AC-ACC-754
  - TC-AC-ACC-755
  - TC-AC-ACC-756
  - TC-AC-ACC-626
coverage:
  web: automated
---

# Popup Edit Client: Saving State, Aksesibilitas, dan Form Tidak Ter-Refresh oleh Perubahan Sesi Lain (Total Control)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (A-01) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login akun Total Control Principal di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya. `{r6}` = 6 digit terakhir `{runId}` (dipakai agar Client Code tetap maksimal 15 karakter).
- Dataset seed (nama bersuffix): Client `PT Opsi Dinamis {runId}-078` (replika C-LST-4: Fax kosong; target TC-753); Client `PT Teknologi Maju {runId}-078` (replika C-02: Active, Partner CV Mitra Sejati sebagai Anchor dan CV Mitra Lestari, Group Area Jakarta, Client Code `TKM-{r6}`, Default User Not Yet Activated dengan Division seed `Finance` dan Position seed `Finance Manager`) (target TC-754, TC-755, TC-756; popup Edit relasi Partner tanpa Select Group); Client `PT Direct Jakarta {runId}-078` (replika C-ROL-13: Direct, Group Area Jakarta; target TC-626). Seeding Client lewat API/fixture BE di hook `before` (kemampuan disediakan tim FE/BE; endpoint tidak dikarang).
- Tabel Field wajib (TC-754): Company Name, Client Code, PIC Name, PIC Email, Address, Country, State, City, Postal Code, First Name, Last Name, Email, Division.
- Tabel Field teks wajib (TC-755): Company Name, Client Code, PIC Name, PIC Email, Address, Postal Code, First Name, Last Name, Email.
- Kemampuan teknis: menahan response request Edit (throttle jaringan) pada TC-753; membaca atribut `aria-required` dan `aria-describedby`; menekan Tab, Shift+Tab, dan Esc; sesi API aktor sebagai pelaku kedua yang mengubah PIC Name (TC-626; bukan sesi UI kedua).
- Jendela amat TC-626 adalah 30 detik nyata sesuai TC (bukan jendela standar 5 detik; bagian 6 konvensi, jeda pendek yang disebut eksplisit).
- Cleanup: hook `after` menghapus lewat API (soft-delete) Client yang dibuat atau di-seed spec ini, tanpa mengasumsikan setup berhasil penuh.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

### TC-753: Saving state tombol Save

1. Ketik Search `PT Opsi Dinamis {runId}-078`, tekan Enter
2. Buka `⋯` baris `PT Opsi Dinamis {runId}-078` lalu klik `Edit`
3. Ubah Fax menjadi `0215550199`
4. Tahan response request Edit (throttle jaringan)
5. Klik `[Save]` lalu lihat popup sebelum response diterima
6. Verifikasi tombol `[Save]` menampilkan indikator loading dan berstatus disabled
7. Verifikasi tombol `[Clear Field]`, ikon close `[✕]`, dan input Fax disabled
8. Lepas throttle dan tunggu response
9. Verifikasi popup tertutup
10. Verifikasi toast sukses "Success, client has been updated."

### TC-754: aria-required pada popup Edit

11. Ketik Search `PT Teknologi Maju {runId}-078`, tekan Enter
12. Buka `⋯` baris `PT Teknologi Maju {runId}-078` lalu klik `Edit`
13. Untuk setiap field pada tabel Field wajib, lakukan langkah 14
14. Verifikasi atribut `aria-required` field bernilai "true"

### TC-755: aria-describedby pada field error

15. Klik `[Clear Field]` untuk mengosongkan seluruh field
16. Klik `[Save]`
17. Untuk setiap field pada tabel Field teks wajib, lakukan langkah 18 sampai 19
18. Verifikasi pesan error inline tampil di bawah field
19. Verifikasi `aria-describedby` field menunjuk ke elemen pesan error milik field tersebut
20. Klik `[✕]` di header popup
21. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
22. Klik `[Leave]`

### TC-756: Fokus terkunci di dalam popup

23. Buka `⋯` baris `PT Teknologi Maju {runId}-078` lalu klik `Edit`
24. Tekan Tab berulang kali hingga fokus mencapai tombol `[Save]`
25. Verifikasi fokus hanya berpindah di antara kontrol di dalam popup dan tidak pernah berpindah ke halaman List di belakang popup
26. Tekan Tab satu kali lagi
27. Verifikasi fokus menuju kontrol fokus pertama di dalam popup
28. Tekan Shift+Tab pada kontrol fokus pertama di dalam popup
29. Verifikasi fokus menuju kontrol fokus terakhir di dalam popup (tombol `[Save]`)
30. Tekan Esc
31. Verifikasi popup tertutup langsung
32. Verifikasi dialog Unsaved Changes tidak muncul (tidak ada nilai yang diubah)

### TC-626: Form tidak ter-refresh oleh perubahan sesi lain

33. Ketik Search `PT Direct Jakarta {runId}-078`, tekan Enter
34. Buka `⋯` baris `PT Direct Jakarta {runId}-078` lalu klik `Edit`
35. Isi Fax dengan `0215550177` tanpa menekan `[Save]`
36. Pelaku kedua (sesi API) mengubah PIC Name "PT Direct Jakarta {runId}-078" menjadi "Rina Kartika" hingga tersimpan
37. Tunggu aksi selesai
38. Amati popup Edit selama 30 detik tanpa aksi
39. Verifikasi popup Edit tetap terbuka
40. Verifikasi Fax tetap "0215550177"
41. Verifikasi field PIC Name di popup tetap bernilai awal (tidak ter-refresh)
42. Verifikasi tidak ada dialog maupun toast yang muncul
43. Klik `[✕]` di header popup
44. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Leave]` dan `[Cancel]` tampil
45. Klik `[Leave]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Alasan di atas 35 langkah (sekitar 45 langkah): satu role, satu topik (perilaku popup Edit), tiga Client seed milik sendiri; langkah 14 diulang untuk 13 field dan 18 sampai 19 untuk 9 field (butir 8b-7).
- Pelaku kedua TC-626 memakai sesi API hingga PIC Name tersimpan (R-20); bukan konteks UI kedua (TC bertanda Manual Only, dua sesi paralel).
- Langkah penghubung (S-03): Search nama unik; penutup form dirty (S-08); TC-756 membuka popup baru karena Esc dengan form dirty akan memunculkan dialog.
- Temuan untuk QA:
  - TC-754 menyertakan Client Code pada field wajib, sedangkan popup Create (TC-750) tidak; spec mengikuti anggota masing-masing TC.

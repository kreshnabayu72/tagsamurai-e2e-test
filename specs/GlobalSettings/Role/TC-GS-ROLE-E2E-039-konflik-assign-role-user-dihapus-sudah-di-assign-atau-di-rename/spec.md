---
id: TC-GS-ROLE-E2E-039-konflik-assign-role-user-dihapus-sudah-di-assign-atau-di-rename
title: "Konflik Assign Role: User Dihapus, Sudah di-Assign, atau di-Rename oleh Admin Lain"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-99
  - TC-GS-ROLE-100
coverage:
  web: automated
---

# Konflik Assign Role: User Dihapus, Sudah di-Assign, atau di-Rename oleh Admin Lain

## Prerequisites

- Mode: FE+BE.
- Kelas harness: multi-konteks (konflik dua admin), objek uji spec ini.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role` mengikuti pernyataan hook suite di `suite.md`.
- Akun sesi A (UI): Ahmad Fauzi (Total Control, Pre-setup #1), email `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dilakukan di hook `before`; hook `beforeEach` membuka Global Settings > Role & Permission > Tab System > Detail `Manage hardware`. Spec memakai satu akun UI; tidak ada ganti akun.
- Akun sesi B (API): Eko Prasetyo (Total Control kedua, Pre-setup #13), password `Spectra.env.GS_TC2_PASSWORD`, login lewat sesi API di hook `before`. Sesi B hanya memicu perubahan state (assign Yoga Pratama, hapus user Citra Dewanti, rename Tari Anjani); hasilnya tidak diasersi di sesi UI kedua. Kemampuan teknis yang disediakan tim FE/BE: sesi API Eko Prasetyo untuk assign role `Manage hardware`, hapus user, dan rename user (nama endpoint tidak disebut di TC, PRD, atau LLD yang dirujuk spec ini).
- Kemampuan teknis: dua sesi berjalan bersamaan (sesi A di browser, sesi B lewat API) dengan urutan aksi yang dikendalikan spec; memuat ulang halaman.
- Data Pre-setup #18 (kandidat fixture sekali pakai): Yoga Pratama (Pending Activation), Tari Anjani (Inactive), dan Citra Dewanti (Active); ketiganya Access Global Settings dicentang, tanpa access level, tanpa baris role.
- Data yang diubah spec: Yoga Pratama mendapat baris `Manage hardware` (oleh sesi B); Citra Dewanti dihapus (oleh sesi B); Tari Anjani di-rename menjadi Tari Anjana lalu di-assign `Manage hardware` (TC-GS-ROLE-100). Hook `after` memulihkan ke kondisi Pre-setup #18 lewat seeding API (disediakan tim FE/BE): menghapus baris `Manage hardware` Yoga Pratama dan Tari Anjana, mengembalikan nama Tari Anjana menjadi Tari Anjani, dan membuat ulang Citra Dewanti.
- State global: tidak ada yang diubah (suite berjalan serial, `suite.md`).

## Test Steps

### TC-GS-ROLE-99: Assign Role saat user terpilih dihapus atau sudah di-assign admin lain

1. Sesi A: klik `[+ Assign]`
2. Sesi A: centang Yoga Pratama
3. Sesi A: centang Tari Anjani
4. Sesi B (API, Eko Prasetyo): assign Yoga Pratama ke `Manage hardware`
5. Sesi A: klik `[Assign]`
6. Verifikasi alert inline "Yoga Pratama is no longer eligible. Please select another."
7. Verifikasi Tari Anjani tetap tercentang
8. Verifikasi centangan Yoga Pratama hilang
9. Verifikasi picker di-refetch: Yoga Pratama tidak lagi muncul di daftar picker
10. Sesi A: centang Citra Dewanti
11. Sesi B (API, Eko Prasetyo): hapus user Citra Dewanti
12. Sesi A: klik `[Assign]` lagi
13. Verifikasi alert inline "Citra Dewanti no longer exists. Please select another."
14. Verifikasi centangan Citra Dewanti hilang
15. Verifikasi Tari Anjani tetap tercentang
16. Sesi A: tutup popup dengan `✕`
17. Sesi A: muat ulang halaman
18. Verifikasi baris Yoga Pratama tampil di Detail `Manage hardware`
19. Verifikasi Tari Anjani tidak ditambahkan (tidak ada baris Tari Anjani)
20. Verifikasi tidak ada baris baru untuk Citra Dewanti

### TC-GS-ROLE-100: Assign Role saat user terpilih di-rename sebelum submit

21. Sesi A: klik `[+ Assign]`
22. Sesi A: centang Tari Anjani
23. Sesi B (API, Eko Prasetyo): rename Tari Anjani menjadi Tari Anjana
24. Sesi A: klik `[Assign]`
25. Verifikasi toast sukses "Success, role has been assigned."
26. Verifikasi Detail `Manage hardware` menampilkan baris "Tari Anjana"

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Kedua TC bertanda Automation `Manual Only — (d) dua sesi paralel` tetap masuk spec; kebutuhan dua sesi tertulis di Prerequisites. Kelas harness spec ini: multi-konteks (konflik dua admin) sebagai objek uji; butir pengecualian `P-2` tidak dipakai.
- Subjudul `###` memetakan langkah ke id TC sumber.
- Langkah penghubung (tanpa awalan `Verifikasi`): menutup popup dengan `✕` (langkah 16, popup picker tidak memunculkan dialog Unsaved Changes) dan memuat ulang halaman (langkah 17). Keduanya dibutuhkan karena Expected b ("Tari Anjani tidak ditambahkan") dan Expected d ("tidak ada baris baru") hanya dapat diamati di tabel Detail, sedangkan menutup popup membuang seleksi; pengamatan itu karenanya ditaruh sesudah langkah 15 dan bukan sesudah langkah 7.
- Langkah 9 mengamati "picker di-refetch" sebagai Yoga Pratama tidak lagi muncul di daftar picker (Yoga Pratama sudah di-assign sesi B dan tidak eligible); Tari Anjani yang tetap tercentang (langkah 7) menjadi anchor positif pada surface yang sama.
- Langkah 19 dan 20 (absence baris) didahului langkah 18 (baris Yoga Pratama tampil di tabel yang sama) sebagai anchor positif.
- Temuan untuk QA:
  - TC-GS-ROLE-99 dan TC-GS-ROLE-100 tidak punya Post Condition; tidak ada yang diasersi tambahan.
  - TC-GS-ROLE-99 Expected c ("picker di-refetch") tidak menyebut cara pengamatannya; spec mengamati lewat daftar picker (langkah 9).
  - TC-GS-ROLE-99 Expected b dan d ("tidak ditambahkan", "tidak ada baris baru") tidak menyebut tempat pengamatan; spec mengamatinya di tabel Detail setelah popup ditutup.
  - TC-GS-ROLE-99 dan TC-GS-ROLE-100 menyebut "Eko Prasetyo login di sesi B" tanpa menyebut aksi sesi B sebagai UI atau API; spec memakai sesi API karena hasil sesi B tidak diasersi.

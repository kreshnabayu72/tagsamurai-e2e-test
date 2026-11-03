---
id: TC-AC-ACC-E2E-035-defense-tulis-langsung-di-luar-scope-group-ditolak-404
title: "Defense-in-depth: Aksi Tulis Langsung ke Client di Luar Scope Group oleh Group Manager Ditolak 404"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-454
  - TC-AC-ACC-987
coverage:
  web: automated
---

# Defense-in-depth: Aksi Tulis Langsung ke Client di Luar Scope Group oleh Group Manager Ditolak 404

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-01 | Total Control (Principal) | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, A-01); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Target request ditolak memakai Client milik spec (S-06), di-seed lewat Fixture BE di hook `before` dan dihapus di hook `after`: `PT Uji Luar Scope {runId}-035` (Active, Group `Area Surabaya`, di luar scope `Area Jakarta` dan descendant-nya, Partner CV Mitra Timur, FAMS Active; menggantikan `PT Timur Perkasa`). ID Client dan ID tidak terdaftar `3f9a1c2e-7b44-4d0e-9a51-6c2d8e1f0b77` dipakai di request; ID Client diambil dari Fixture BE.
- Kemampuan teknis: sesi API Group Manager (A-03, `groupManagerJakarta_automated_qaTeam1@qwertysystem.net`, `Spectra.env.AC_CLIENT_GM_PASSWORD`) lewat login API (token tidak dihitung sebagai sesi web; disediakan tim BE/FE) dan klien HTTP untuk request langsung; sesi UI Total Control (A-01) tetap satu konteks. Pelaku kedua lewat sesi API bukan konteks kedua kelas c (bagian 3, P-2). Env var `AC_CLIENT_GM_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; tim FE mendaftarkannya saat tahap script.
- Data uji: PIC Name uji `Uji Tulis Luar Scope`; Change Partner menambah `CV Mitra Lestari`; Delete memakai body companyName `PT Uji Luar Scope {runId}-035` dan confirm true; Changelog Client dibaca lewat modal Changelog List dengan Search nama Client dan ukuran halaman 100.
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-454: Group Manager tidak bisa menulis Client di luar group assignment: Edit langsung ditolak 404

1. Ambil token sesi API Group Manager
2. Kirim request HTTP Edit Client dengan ID `PT Uji Luar Scope {runId}-035` memakai token tersebut (PIC Name `Uji Tulis Luar Scope`), tanpa melalui UI
3. Verifikasi respons HTTP `404 Not Found`
4. Verifikasi body respons tidak memuat data Client
5. Kirim request HTTP yang sama ke endpoint Edit Client dengan ID Client yang tidak terdaftar
6. Verifikasi respons HTTP `404 Not Found` dengan status dan body yang sama dengan request pertama (tidak ada petunjuk bahwa Client berada di luar scope)
7. Tunggu aksi selesai
8. Ketik Search `PT Uji Luar Scope {runId}-035`, tekan Enter
9. Klik Company Name `PT Uji Luar Scope {runId}-035` untuk membuka Detail
10. Verifikasi Detail `PT Uji Luar Scope {runId}-035` terbuka
11. Verifikasi PIC Name bukan `Uji Tulis Luar Scope` (request tidak mengubah data)
12. Kembali ke List dengan tombol Back browser

### TC-AC-ACC-987: Aksi tulis langsung (Change Partner, Suspend, Unsuspend, Delete) ke Client di luar scope ditolak 404 dan tidak mengubah data

13. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik Search `PT Uji Luar Scope {runId}-035`, tekan Enter, ubah ukuran halaman modal menjadi 100, catat jumlah baris (L0), lalu tutup modal
14. Kirim request HTTP Change Partner (tambah `CV Mitra Lestari`) untuk `PT Uji Luar Scope {runId}-035` memakai token sesi API Group Manager, tanpa melalui UI
15. Verifikasi respons `404 Not Found` dan body tidak memuat data Client
16. Kirim request HTTP Suspend untuk `PT Uji Luar Scope {runId}-035` memakai token sesi yang sama, tanpa melalui UI
17. Verifikasi respons `404 Not Found` dan body tidak memuat data Client
18. Kirim request HTTP Unsuspend untuk `PT Uji Luar Scope {runId}-035` memakai token sesi yang sama, tanpa melalui UI
19. Verifikasi respons `404 Not Found` dan body tidak memuat data Client
20. Kirim request HTTP Delete untuk `PT Uji Luar Scope {runId}-035` memakai token sesi yang sama, tanpa melalui UI
21. Verifikasi respons `404 Not Found` dan body tidak memuat data Client
22. Verifikasi tidak ada respons sukses (2xx) untuk permintaan mana pun pada keempat request
23. Tunggu aksi selesai
24. Klik sub-tab `Active`, ketik Search `PT Uji Luar Scope {runId}-035`, tekan Enter, dan lihat sel Managed By dan FAMS baris `PT Uji Luar Scope {runId}-035`
25. Verifikasi `PT Uji Luar Scope {runId}-035` tetap tampil di sub-tab `Active`
26. Verifikasi sel Managed By adalah `CV Mitra Timur` tanpa teks `+N more`
27. Verifikasi sel FAMS adalah badge `Active`
28. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik Search `PT Uji Luar Scope {runId}-035`, tekan Enter, ubah ukuran halaman modal menjadi 100, lalu hitung baris (L1)
29. Verifikasi L1 sama dengan L0 (tidak ada baris Changelog baru)
30. Tutup modal Changelog dan klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 7, 8, 12, 23, 30. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- K-1: spec kelas a (defense-in-depth) yang Expected-nya berupa respons API dan state data (TC-AC-ACC-454, 987: Edit/Change Partner/Suspend/Unsuspend/Delete langsung ke Client di luar scope dijawab 404, data tidak berubah) tetap masuk spec FE+BE walau tumpang tindih dengan `tc-client-backend.md`; asersi request hanya status respons dan state data (bagian 8b butir 1).
- Sesi A pada TC-AC-ACC-987 ("Sesi A: Group Manager") dijalankan sebagai sesi API Group Manager (hanya memicu request, tanpa UI), sedangkan Sesi B adalah sesi UI Total Control di hook `before`; keduanya tidak paralel (TC menandai `Manual Only (d) dua sesi paralel`). Pelaku kedua lewat sesi API bukan konteks kedua (bagian 3 P-2, KEPUTUSAN 2026-10-30).
- Penyimpangan data (S-06): TC menyebut `PT Timur Perkasa` (C-12) sebagai target; spec memakai Client milik spec bersuffix dengan atribut yang sama (Active, Group Area Surabaya, Partner CV Mitra Timur, FAMS Active) karena request langsung yang diuji ditolak tetap memakai data milik spec. Langkah 1 dan 8 TC-AC-ACC-987 (baca Changelog) memakai baseline L0 (S-12).
- Pembagian TC lintas spec: defense tulis tanpa permission (TC-AC-ACC-450, 621 sampai 625) di spec 034; XSS di spec 036.
- Temuan untuk QA:
  - TC-AC-ACC-987: kolom Automation `Manual Only (d) dua sesi paralel`, tetapi Sesi A hanya memicu request langsung dan Sesi B membaca Changelog; spec menjalankan Sesi A sebagai sesi API sehingga cukup satu konteks UI.
  - TC-AC-ACC-454: langkah 4 TC ("Keluar dari akun Group Manager lalu login sbg Total Control") dilebur karena sesi UI sudah Total Control sejak hook `before` (P-3 tidak dipakai; Sesi API tidak butuh Logout).
  - TC-AC-ACC-987: Expected butir c menyebut sel Managed By `CV Mitra Timur` dan FAMS `Active` untuk `PT Timur Perkasa`; spec menetapkan atribut yang sama pada Client milik spec.

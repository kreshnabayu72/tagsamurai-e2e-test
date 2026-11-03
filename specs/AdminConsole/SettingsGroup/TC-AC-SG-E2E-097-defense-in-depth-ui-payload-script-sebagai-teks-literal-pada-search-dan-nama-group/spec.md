---
id: TC-AC-SG-E2E-097-defense-in-depth-ui-payload-script-sebagai-teks-literal-pada-search-dan-nama-group
title: "Defense-in-Depth UI: Payload Script Dirender sebagai Teks Literal pada Search dan Nama Group"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-183
  - TC-AC-SG-369
coverage:
  web: automated
---

# Defense-in-Depth UI: Payload Script Dirender sebagai Teks Literal pada Search dan Nama Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal, `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite (suite.md).
- Data Pre-setup: Pohon Uji Utama entitas Principal (Pre-setup #16 dan #17) dibaca saja oleh TC-AC-SG-183. Data uji Search: `<script>alert(1)</script>` dan `' OR 1=1 --` (diketik apa adanya).
- Data yang dibuat langkah spec (TC-AC-SG-369): group level 1 bernama `<img src=x onerror=alert(1)> {runId}-097` (payload TC `<img src=x onerror=alert(1)>` diikuti suffix per run agar nama unik pada parent yang sama). Hook `before` menghapus sisa group bernama payload dari run sebelumnya dan hook `after` menghapus group yang dibuat spec lewat Fixture BE.
- Kemampuan teknis: Fixture BE (pembersihan group; disediakan tim FE/BE); kemampuan mendeteksi dialog `alert` yang muncul selama langkah berjalan (disediakan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-SG-183: Kata kunci Search diperlakukan sebagai teks literal (payload tidak dieksekusi)

1. Ketik Search `<script>alert(1)</script>`, tekan Enter
2. Verifikasi tabel menampilkan empty state "No results found"
3. Verifikasi tidak ada dialog script dan tidak ada pesan error
4. Ganti isi kotak search dengan `' OR 1=1 --`, tekan Enter
5. Verifikasi tabel menampilkan empty state "No results found"
6. Verifikasi tidak ada dialog script dan tidak ada pesan error
7. Klik `(←)` pada kotak Search

### TC-AC-SG-369: Nama group berisi payload script disimpan dan dirender sebagai teks literal

8. Klik `[+] Group` di Sidebar Group Tree
9. Ketik `<img src=x onerror=alert(1)> {runId}-097` lalu klik `[Submit]`
10. Ketik Search `{runId}-097`, tekan Enter
11. Verifikasi tabel menampilkan nama `<img src=x onerror=alert(1)> {runId}-097` sebagai teks apa adanya
12. Verifikasi Sidebar Group Tree menampilkan nama `<img src=x onerror=alert(1)> {runId}-097` sebagai teks apa adanya
13. Klik ikon `⋯` pada baris `<img src=x onerror=alert(1)> {runId}-097` lalu `Delete`
14. Verifikasi dialog Delete menampilkan nama `<img src=x onerror=alert(1)> {runId}-097` sebagai teks apa adanya
15. Klik `[Cancel]` pada dialog Delete
16. Klik ikon Changelog pada toolbar
17. Verifikasi Modal "Changelog: Group" menampilkan Group Name `<img src=x onerror=alert(1)> {runId}-097` sebagai teks apa adanya
18. Verifikasi tidak ada script yang berjalan (tidak ada dialog `alert`) pada langkah 9 sampai 17
19. Tutup Modal Changelog dengan `✕`
20. Klik `(←)` pada kotak Search

## Notes

- K-1 tidak dipakai: TC kelas a ini berupa Expected UI (empty state, teks literal) dan tidak berupa respons API.
- Langkah penghubung (S-03, R-16, tanpa `Verifikasi`): langkah 7 dan 20 (mengosongkan Search dengan `(←)`), langkah 10 (Search `{runId}-097` untuk menemukan baris target), langkah 15 (`[Cancel]` menutup dialog Delete tanpa menghapus), dan langkah 19 (menutup Modal Changelog).
- Absence dialog script (langkah 3, 6, dan 18) didahului `Verifikasi` anchor pada surface yang sama: empty state "No results found" (langkah 2 dan 5) dan nama group tampil sebagai teks (langkah 11, 12, 14, dan 17).
- Payload dikirim ke surface Search dan nama group; tanda `<`/`>` pada nama diketik apa adanya dan tidak diterjemahkan.
- Temuan untuk QA:
  - TC-AC-SG-183 Langkah Uji 2 menyebut "input pencarian terbuka dengan fokus kursor dan placeholder"; keadaan itu bukan Expected TC ini dan tidak diasersi (S-02).
  - TC-AC-SG-369 Expected "tidak ada script yang berjalan" tidak menyebut cara mendeteksi; spec memakai deteksi dialog `alert` (kemampuan disediakan tim FE).
  - TC-AC-SG-369 memakai nama `<img src=x onerror=alert(1)>` persis; spec menambah suffix ` {runId}-097` setelah payload agar nama unik per run (S-12) dan tetap memuat payload utuh.

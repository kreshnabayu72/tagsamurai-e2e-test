---
id: TC-GS-TAG-E2E-047-bulk-action-bar-registri-counter-select-all-dan-icon-aksi
title: "Bulk Action Bar Tab Not Paired: Counter, Select All, Reserved/Combined Dilewati, Siklus Unselect All, dan Icon/Severity Row Action"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-149
  - TC-GS-TAG-150
  - TC-GS-TAG-159
  - TC-GS-TAG-335
coverage:
  web: automated
---

# Bulk Action Bar Tab Not Paired: Counter, Select All, Reserved/Combined Dilewati, Siklus Unselect All, dan Icon/Severity Row Action

## Prerequisites

- Mode: FE+BE (backend nyata). Spec ini tidak menghapus data.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite.
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab Not Paired.
- Data Pre-setup: Seed Registri A (Client A, DD-01..DD-30) dengan 26 baris Not Paired. `Select All` memuat 23 baris eligible: 26 dikurangi DD-06 (Reserved), DD-11 dan DD-13 (combined) yang tidak punya checkbox (N = 23 diturunkan dari seeding, bukan dibaca dari satu halaman tabel). Baris yang dipakai: DD-02 `E2801160600002054D8A0002` (Available), DD-04 `AABBCCDDEE80` (Damaged/Missing), DD-06 (Reserved), DD-11 dan DD-13 (combined). Identifier tetap, tidak bisa bersufiks `{runId}` (S-12, Q-4); seeding idempotent lewat fixture BE memulihkan kondisi awal sebelum spec.
- Kemampuan teknis (disediakan tim FE/BE): seed dan reset idempotent Seed Registri A.
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): kembalikan Seed Registri A lewat fixture BE.
- Suite serial (`parallel: false`). Spec tidak mengubah state global selain sesi akun.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate`, lihat `suite.md`.

## Test Steps

### TC-GS-TAG-149: Bulk Action Bar dan counter pluralisasi

1. Centang baris DD-02
2. Verifikasi Bulk Action Bar tampil berurutan: `Bulk Action` (dropdown) | counter | `Select All (23 records)` | `(✕)`
3. Verifikasi counter `1 TAG selected`
4. Centang baris DD-04
5. Verifikasi counter `2 TAGs selected`
6. Klik `(✕)`
7. Verifikasi seluruh seleksi dibatalkan
8. Verifikasi Bulk Action Bar hilang

### TC-GS-TAG-150: Baris Reserved dan combined tanpa checkbox, dilewati Select All

9. Amati kolom checkbox baris DD-06 (Reserved)
10. Verifikasi checkbox baris DD-06 Hidden
11. Verifikasi checkbox baris combined DD-11 dan DD-13 Hidden
12. Centang baris DD-02
13. Klik `Select All (23 records)`
14. Verifikasi counter `23 TAGs selected`
15. Verifikasi tombol berubah menjadi `Unselect All`

### TC-GS-TAG-159: Siklus Select All dan Unselect All

16. Klik `Unselect All`
17. Centang baris DD-02
18. Klik `Select All (23 records)`
19. Verifikasi tombol berubah menjadi `Unselect All`
20. Uncheck baris DD-02
21. Verifikasi tombol kembali menjadi `Select All (23 records)`
22. Verifikasi counter `22 TAGs selected`
23. Klik `Select All (23 records)`
24. Klik `Unselect All`
25. Verifikasi seluruh seleksi lintas halaman dibatalkan
26. Verifikasi Bulk Action Bar tertutup

### TC-GS-TAG-335: Icon dan severity row action serta Bulk Action Bar

27. Buka menu baris DD-02
28. Verifikasi entri `TAG Log` berikon `FileInfoLine` dengan severity dark
29. Verifikasi entri `Delete` berikon `DeleteBin6Line` dengan severity danger
30. Verifikasi entri `TAG Log` berada di atas entri `Delete`
31. Tutup menu
32. Centang baris DD-02
33. Buka dropdown `Bulk Action`
34. Verifikasi dropdown memuat satu entri `Delete` berikon `DeleteBin6Line` dengan severity danger
35. Tutup dropdown
36. Klik `(✕)` untuk membatalkan seleksi

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular.
- Alasan spec melewati sekitar 35 langkah (36 langkah): empat TC atas satu permukaan (Bulk Action Bar Tab Not Paired) dan satu dataset (Seed Registri A), tanpa kelas harness khusus dan tanpa menghapus data; tiap blok mulai dari seleksi yang dibentuk sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 12 dan 17 (mencentang baris DD-02 supaya Bulk Action Bar dan `Select All (23 records)` tampil; bar hilang bila seleksi kosong, TC-GS-TAG-149 Expected c), 16 (mengosongkan seleksi dari TC-GS-TAG-150 sebelum TC-GS-TAG-159 mulai dari Select All baru), 31 dan 35 (menutup menu dan dropdown), 36 (membersihkan seleksi).
- Asersi tambahan di luar Expected TC (S-03): tidak ada.
- Rujukan lintas spec: TC-GS-TAG-172 (checkbox combined Hidden dan dilewati Select All) ada di spec 046; asersi dilewati Select All untuk DD-11 dan DD-13 diasersi di sini (langkah 14).
- Temuan untuk QA:
  - Q-4: hitungan 23 record, 26 baris Not Paired, dan kondisi checkbox valid hanya bila Seed Registri A dipulihkan sebelum spec.
  - TC-GS-TAG-159 Expected b menulis `Select All ([N] records)` tanpa nilai N; spec mengasersi `Select All (23 records)` (N = 23 dari seeding) dan counter `22 TAGs selected`. TC tidak menyebut ukuran halaman default sehingga "lintas halaman" (Expected c) tidak diverifikasi pada halaman tertentu.
  - TC-GS-TAG-149 Expected c: `(✕)` "membatalkan seleksi dan bar hilang" dipecah menjadi dua `Verifikasi` (langkah 7 dan 8).
  - TC-GS-TAG-150 dan TC-GS-TAG-159 tidak menyebut seleksi awal sebelum klik `Select All`, padahal Bulk Action Bar (tempat tombol itu berada) hilang bila seleksi kosong; spec mencentang baris DD-02 lebih dulu (langkah 12 dan 17).
  - Post Condition semua TC bernilai `-`.

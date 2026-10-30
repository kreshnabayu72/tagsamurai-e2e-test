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
12. Klik `Select All (23 records)`
13. Verifikasi counter `23 TAGs selected`
14. Verifikasi tombol berubah menjadi `Unselect All`

### TC-GS-TAG-159: Siklus Select All dan Unselect All

15. Klik `Unselect All`
16. Klik `Select All (23 records)`
17. Verifikasi tombol berubah menjadi `Unselect All`
18. Uncheck baris DD-02
19. Verifikasi tombol kembali menjadi `Select All (23 records)`
20. Verifikasi counter `22 TAGs selected`
21. Klik `Select All (23 records)`
22. Klik `Unselect All`
23. Verifikasi seluruh seleksi lintas halaman dibatalkan
24. Verifikasi Bulk Action Bar tertutup

### TC-GS-TAG-335: Icon dan severity row action serta Bulk Action Bar

25. Buka menu baris DD-02
26. Verifikasi entri `TAG Log` berikon `FileInfoLine` dengan severity dark
27. Verifikasi entri `Delete` berikon `DeleteBin6Line` dengan severity danger
28. Verifikasi entri `TAG Log` berada di atas entri `Delete`
29. Tutup menu
30. Centang baris DD-02
31. Buka dropdown `Bulk Action`
32. Verifikasi dropdown memuat satu entri `Delete` berikon `DeleteBin6Line` dengan severity danger
33. Tutup dropdown
34. Klik `(✕)` untuk membatalkan seleksi

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 15 (mengosongkan seleksi dari TC-GS-TAG-150 sebelum TC-GS-TAG-159 mulai dari Select All baru), 29 dan 33 (menutup menu dan dropdown), 34 (membersihkan seleksi).
- Asersi tambahan di luar Expected TC (S-03): tidak ada.
- Rujukan lintas spec: TC-GS-TAG-172 (checkbox combined Hidden dan dilewati Select All) ada di spec 046; asersi dilewati Select All untuk DD-11 dan DD-13 diasersi di sini (langkah 13).
- Temuan untuk QA:
  - Q-4: hitungan 23 record, 26 baris Not Paired, dan kondisi checkbox valid hanya bila Seed Registri A dipulihkan sebelum spec.
  - TC-GS-TAG-159 Expected b menulis `Select All ([N] records)` tanpa nilai N; spec mengasersi `Select All (23 records)` (N = 23 dari seeding) dan counter `22 TAGs selected`. TC tidak menyebut ukuran halaman default sehingga "lintas halaman" (Expected c) tidak diverifikasi pada halaman tertentu.
  - TC-GS-TAG-149 Expected c: `(✕)` "membatalkan seleksi dan bar hilang" dipecah menjadi dua `Verifikasi` (langkah 7 dan 8).
  - Post Condition semua TC bernilai `-`.

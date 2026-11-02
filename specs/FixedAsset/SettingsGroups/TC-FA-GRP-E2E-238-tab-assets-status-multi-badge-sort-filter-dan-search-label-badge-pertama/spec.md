---
id: TC-FA-GRP-E2E-238-tab-assets-status-multi-badge-sort-filter-dan-search-label-badge-pertama
title: "Tab Assets Status Multi-Badge: Sort Menurut Label Badge Pertama, Filter OR, dan Search Label Badge Mana Pun"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-1140
  - TC-FA-GRP-1141
  - TC-FA-GRP-1142
coverage:
  web: automated
---

# Tab Assets Status Multi-Badge: Sort Menurut Label Badge Pertama, Filter OR, dan Search Label Badge Mana Pun

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global) mengikuti `suite.md`.
- Data Pre-setup (hanya dibaca, tidak diubah): Multi Badge Node (Tabel B No 7, Assignable, level 1) berisi hanya aset A1 (overlay Borrowed + Damaged; badge dalam sel tampil alfabetis: Borrowed lalu Damaged), A2 (Assigned), A3 (Damaged), A4 (Draft). Empat nilai Status distinct memenuhi syarat sort/filter/search (S-11). Fixture "Pre-setup tambahan" ini di-seed oleh tim FE/BE dan tidak diubah spec.
- Kolom Status tampil pada konfigurasi kolom default tab Assets.
- Kemampuan teknis: membaca nama aset A1 sampai A4 lewat fixture BE; disediakan tim FE/BE tanpa endpoint karangan.
- State global: tidak ada. Spec tidak menyimpan Setup Column; filter dan Search yang tersisa dibersihkan langkah penghubung.

## Test Steps

### TC-FA-GRP-1140: Sort Status sel multi-badge menurut label badge pertama

1. Buka Detail Multi Badge Node (Tab Assets)
2. Verifikasi kolom Status tampil pada tabel (precondition TC)
3. Klik header Status 1×
4. Verifikasi urutan Ascending A→Z menurut label badge pertama: A2 (Assigned), A1 (Borrowed + Damaged), A3 (Damaged), A4 (Draft)
5. Verifikasi A1 diurutkan menurut `Borrowed`, bukan `Damaged` maupun gabungan label
6. Klik header 2×
7. Verifikasi urutan Descending Z→A (kebalikan urutan Ascending): A4, A3, A1, A2
8. Klik header 3×
9. Verifikasi urutan kembali ke default tabel (Name A→Z)

### TC-FA-GRP-1141: Filter Status sel multi-badge cocok bila salah satu badge sama (OR)

10. Klik icon Filter
11. Buka dropdown Status
12. Verifikasi opsi Status berisi nilai badge distinct `Borrowed`, `Damaged`, `Assigned`, `Draft` sebagai opsi terpisah
13. Verifikasi tidak ada opsi gabungan `Borrowed, Damaged`
14. Pilih Damaged
15. Klik [Apply]
16. Verifikasi A1 dan A3 tampil (salah satu badge A1 sama dengan opsi)
17. Verifikasi A2 dan A4 tidak tampil
18. Klik icon Filter, ganti pilihan Status menjadi Borrowed saja, klik [Apply]
19. Verifikasi hanya A1 yang tampil (A2, A3, A4 tidak tampil)
20. Klik icon Filter, pilih Assigned dan Borrowed (hanya dua opsi itu terpilih), klik [Apply]
21. Verifikasi A1 dan A2 tampil (OR di dalam field)

### TC-FA-GRP-1142: Search Status sel multi-badge dicocokkan ke label badge mana pun

22. Klik icon Filter, kosongkan pilihan Status, klik [Apply] (langkah penghubung)
23. Verifikasi kolom Status tampil pada tabel (precondition TC)
24. Ketik Search `damaged`, tekan Enter
25. Verifikasi A1 dan A3 tampil (A1 cocok lewat badge kedua `Damaged`)
26. Verifikasi A2 dan A4 tidak tampil
27. Ganti isi kotak search dengan `borrowed`, tekan Enter
28. Verifikasi hanya A1 yang tampil (cocok lewat badge pertama `Borrowed`)
29. Klik `(←)` pada kotak Search (langkah penghubung)

## Notes

- Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): "Klik icon Filter, kosongkan pilihan Status, klik [Apply]" dan "Klik `(←)` pada kotak Search" mengosongkan state sebelum TC berikutnya dan di akhir spec (S-09).
- Temuan untuk QA:
  - TC-FA-GRP-1140: nama aset A1 sampai A4 tidak ditentukan, sehingga urutan default Name A→Z hanya diasersi sebagai "kembali ke default tabel" tanpa urutan nama konkret.
  - TC-FA-GRP-1141: langkah 7 "pilih Assigned dan Borrowed" tidak menyebut apakah pilihan sebelumnya dikosongkan; spec memilih tepat dua opsi itu.
  - Klausa "tidak ada opsi gabungan" diverifikasi terpisah dari butir (a) agar tiap klausa punya Verifikasi sendiri (S-01).

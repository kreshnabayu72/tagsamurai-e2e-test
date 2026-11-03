---
id: TC-AC-ACC-E2E-242-filter-station-list-panel-dropdown-range-dan-empty-state
title: "Filter Station List: Screening Panel, Dropdown, Range Ports dan Tablets, Last Active, dan Empty State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-312
  - TC-AC-ACC-790
  - TC-AC-ACC-791
  - TC-AC-ACC-792
  - TC-AC-ACC-851
coverage:
  web: automated
---

# Filter Station List: Screening Panel, Dropdown, Range Ports dan Tablets, Last Active, dan Empty State

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup (hanya dibaca, tidak diubah): Client C-01 "PT Sejahtera Abadi" dengan Station List: "Gerbang Gudang A" (Active, Reader Group (Fixed Asset) "Gudang Pusat", Reader Group (Supply) kosong, Ports 4, Tablets 2, Last Active 08 Jul 2026 pukul 09:30); "Gerbang Gudang B" (Inactive, "Gudang Pusat", "Supply Utama", Ports 4, Tablets 1, Last Active 08 Jul 2026 pukul 08:10); "Gerbang Lama" (Deactivated, kedua group kosong, Ports 2, Tablets 0, Last Active 01 Mar 2026).
- Parameter blok TC-AC-ACC-790 (langkah 12 sampai 15):

| Kolom Filter | Nilai | Baris tampil | Baris tidak tampil |
|---|---|---|---|
| Reader Group (Fixed Asset) | Gudang Pusat | Gerbang Gudang A, Gerbang Gudang B | Gerbang Lama |
| Reader Group (Supply) | Supply Utama | Gerbang Gudang B | Gerbang Gudang A, Gerbang Lama |
| Status | Active | Gerbang Gudang A | Gerbang Gudang B, Gerbang Lama |
| Status | Deactivated | Gerbang Lama | Gerbang Gudang A, Gerbang Gudang B |

- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Detail diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

1. Ketik Search "PT Sejahtera Abadi" di List Client, tekan Enter, klik Company Name "PT Sejahtera Abadi", lalu klik Tab Asset Control

### TC-AC-ACC-312: Screening Filter Station List

2. Klik Filter pada toolbar Station List
3. Verifikasi field Reader Group (Fixed Asset): dropdown multi-select searchable dengan placeholder "All groups"
4. Verifikasi field Reader Group (Supply): dropdown multi-select searchable dengan placeholder "All groups"
5. Verifikasi field Ports: field range dengan placeholder "Min" dan "Max"
6. Verifikasi field Tablets: field range dengan placeholder "Min" dan "Max"
7. Verifikasi field Last Active: date range picker satu field dengan placeholder "Select date"
8. Verifikasi field Status: dropdown multi-select searchable dengan placeholder "All statuses"
9. Verifikasi Reader Name, Reader ID, dan Reader Model tidak memiliki field filter
10. Verifikasi Footer panel: [Clear Field] di kiri dan [Apply] di kanan
11. Klik ulang ikon Filter untuk menutup panel

### TC-AC-ACC-790: Filter kolom dropdown

12. Untuk setiap baris tabel "Parameter blok TC-AC-ACC-790" (langkah 12 sampai 15): klik Filter dan klik [Clear Field]
13. Pilih nilai pada kolom Filter sesuai baris tabel, lalu klik [Apply]
14. Verifikasi baris pada kolom "Baris tampil" tampil
15. Verifikasi baris pada kolom "Baris tidak tampil" tidak tampil
16. Klik Filter dan klik [Clear Field]
17. Klik [Apply]

### TC-AC-ACC-791: Filter kolom range

18. Klik Filter, isi Ports Min 3 dan Max 4, lalu klik [Apply]
19. Verifikasi Gerbang Gudang A dan Gerbang Gudang B (Ports 4) tampil
20. Verifikasi Gerbang Lama (Ports 2) tidak tampil
21. Klik Filter, klik [Clear Field], isi Tablets Min 1 dan Max 1, lalu klik [Apply]
22. Verifikasi Gerbang Gudang B (Tablets 1) tampil
23. Verifikasi Gerbang Gudang A (Tablets 2) dan Gerbang Lama (Tablets 0) tidak tampil
24. Klik Filter, klik [Clear Field], lalu klik [Apply]

### TC-AC-ACC-792: Filter kolom Last Active

25. Klik Filter, pilih rentang Last Active 08 Jul 2026 sampai 08 Jul 2026, lalu klik [Apply]
26. Verifikasi Gerbang Gudang A (08 Jul 2026 pukul 09:30) dan Gerbang Gudang B (08 Jul 2026 pukul 08:10) tampil
27. Verifikasi Gerbang Lama (01 Mar 2026) tidak tampil
28. Klik Filter, klik [Clear Field], lalu klik [Apply]

### TC-AC-ACC-851: Empty state hasil search dan filter kosong

29. Klik ikon Search pada Station List, ketik "zzzz", tekan Enter
30. Verifikasi empty state: Illustration dengan Title "No results found" dan Description "Try adjusting your search or filter."
31. Kosongkan isi kotak Search, tekan Enter
32. Verifikasi tiga baris Station List tampil kembali
33. Klik Filter, isi Ports Min 10 dan Max 20, lalu klik [Apply]
34. Verifikasi empty state: Illustration dengan Title "No results found" dan Description "Try adjusting your search or filter."
35. Klik Filter, klik [Clear Field], lalu klik [Apply]

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16, S-09): langkah 1 (Search dan buka Detail Client; hook suite hanya membuka List Client); langkah 11 (menutup panel Filter lewat klik ulang ikon Filter, D-001 `docs/spec-decisions.md`); langkah 16, 17, 24, 28, 35 (membersihkan filter; `[Clear Field]` hanya mengosongkan draft sehingga [Apply] ikut diklik, D-003); langkah 31 (mengosongkan Search sebagai bagian TC).
- Langkah 12 sampai 15 diulang untuk 4 baris tabel parameter (16 langkah setelah ekspansi); tiap iterasi diawali [Clear Field] sehingga draft filter iterasi sebelumnya dibuang (D-003) sebelum nilai berikutnya dipilih. Langkah 16 dan 17 membersihkan filter sesudah iterasi terakhir.
- Spec ini melewati sekitar 35 langkah setelah ekspansi. Alasan: semua blok satu topik (Filter Station List) pada satu dataset Pre-setup baca-saja, dan tiap blok berdiri sendiri karena filter dibersihkan di akhir.
- Temuan untuk QA:
  - TC-AC-ACC-790 tidak mencantumkan [Clear Field] pada iterasi pertama sementara iterasi berikutnya mencantumkannya; spec menjalankan [Clear Field] pada semua iterasi (langkah 12) agar identik.
  - TC-AC-ACC-312 Expected a sampai f tidak menyebut apakah panel Filter menutup sendiri setelah [Apply]; spec mengasumsikan panel tertutup setelah [Apply] sesuai langkah TC berikutnya "Klik Filter" dan menutup panel pada langkah 11 lewat ikon Filter (D-001).

---
id: TC-GS-DIV-E2E-065-changelog-filter-dropdown-search-dan-or-multiselect
title: "Filter Changelog: Kotak Pencarian di Dalam Dropdown Multi-Select dan Logika Disjungsi OR Antar-Opsi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-204
  - TC-GS-DIV-205
  - TC-GS-DIV-292
  - TC-GS-DIV-293
coverage:
  web: automated
---

# Filter Changelog: Kotak Pencarian di Dalam Dropdown Multi-Select dan Logika Disjungsi OR Antar-Opsi

## Prerequisites

- Login sebagai Role: Total Control
- Modal Changelog terisi riwayat dengan variasi aksi, divisi, dan aktor
- User berada di Global Settings > User > Division
- Riwayat Changelog Division terisi (Create dari TC-GS-DIV-30, Edit dan Delete dari TC Section 3; Modified By: Sari D, Rina M, Agus W, Dewi L); entri hasil TC-GS-DIV-101 ada
- Riwayat Changelog Division terisi (Create dari TC-GS-DIV-30, Edit dan Delete dari TC Section 3; Modified By: Sari D, Rina M, Agus W, Dewi L); Division `Public Relations` sudah dibuat dan dihapus (TC-GS-DIV-65, TC-GS-DIV-116)
- Riwayat Changelog Division terisi (Create dari TC-GS-DIV-30, Edit dan Delete dari TC Section 3; Modified By: Sari D, Rina M, Agus W, Dewi L); entri hasil TC-GS-DIV-101 dan TC-GS-DIV-102 ada

## Test Steps

### Search di dalam dropdown filter mempersempit opsi (TC-GS-DIV-204)

1. Klik icon Changelog di Table Tools
2. Buka dropdown Division Name
3. Ketik `account` pada kotak search dropdown
4. Verifikasi Daftar opsi hanya memuat opsi yang memuat `account` tanpa membedakan huruf besar kecil (mis. `Accounting`, `Accounting and Tax`)
5. Verifikasi Keyword yang tidak ada menampilkan keadaan tanpa opsi

### Search dan Filter Modal Changelog dikombinasikan lalu dipulihkan (TC-GS-DIV-205)

6. Klik icon Changelog di Table Tools
7. Filter Action = `Create` lalu Apply
8. Cari `public` lalu Enter
9. Ubah Filter Action menjadi `Edit` lalu Apply (hasil kosong)
10. Buka Filter, klik `[Clear Field]` lalu `[Apply]`
11. Verifikasi Setelah langkah 3 hanya entri Create `Public Relations` tampil (irisan Action `Create` dan keyword `public`)
12. Verifikasi Setelah langkah 4 tampil `No results found` (tidak ada entri Edit `Public Relations`)
13. Verifikasi Setelah langkah 5 hasil keyword `public` pulih (entri Create dan Delete `Public Relations`)

### Search di dalam dropdown filter Changelog: Action, Field, dan Modified By (TC-GS-DIV-292)

14. Klik icon Changelog di Table Tools lalu buka Filter
15. Buka dropdown Action, ketik `cre`
16. Buka dropdown Field, ketik `cod`
17. Buka dropdown Modified By, ketik `sar`
18. Pada tiap dropdown ketik `zzz`
19. Pada tiap dropdown kosongkan kotak search
20. Verifikasi Action: hanya opsi `Create` tampil
21. Verifikasi Field: hanya opsi `Code` tampil
22. Verifikasi Modified By: hanya opsi `Sari D` tampil
23. Verifikasi Keyword `zzz` pada ketiga dropdown menampilkan keadaan tanpa opsi
24. Verifikasi Kotak search dikosongkan: daftar opsi pulih penuh pada ketiga dropdown

### Dua opsi pada satu field filter digabung OR: Division Name, Field, dan Modified By (TC-GS-DIV-293)

25. Klik icon Changelog di Table Tools lalu buka Filter
26. Filter Division Name centang `Accounting and Tax` dan `Procurement`, klik `[Apply]`
27. Clear Field, Filter Field centang `Division Name` dan `Code`, klik `[Apply]`
28. Clear Field, Filter Modified By centang `Sari D` dan `Rina M`, klik `[Apply]`
29. Verifikasi Division Name: tampil baris `Accounting and Tax` atau `Procurement`; tidak ada baris Division lain
30. Verifikasi Field: tampil baris Field `Division Name` atau `Code`
31. Verifikasi Modified By: tampil baris Modified By `Sari D` atau `Rina M`; tidak ada baris `Agus W` dan `Dewi L`

## Notes

- Memvalidasi fungsional pencarian internal di dalam dropdown filter (Action, Field, Division Name, Modified By), penyaringan opsi real-time, dan evaluasi logika disjungsi OR pada baris riwayat saat lebih dari satu opsi dicentang dalam satu field (PRD §4.1.2).
- Sumber pemetaan test case granular: TC-GS-DIV-204, TC-GS-DIV-205, TC-GS-DIV-292, TC-GS-DIV-293.

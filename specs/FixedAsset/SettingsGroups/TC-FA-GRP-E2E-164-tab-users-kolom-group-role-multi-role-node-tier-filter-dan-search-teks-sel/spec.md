---
id: TC-FA-GRP-E2E-164-tab-users-kolom-group-role-multi-role-node-tier-filter-dan-search-teks-sel
title: "Tab Users Kolom Group Role (Multi Role Node): Search per Kolom, Tier Mendahului Group Role, Filter Mencocokkan Setiap Pemegang Role, dan Search Hanya Teks Sel"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-577
  - TC-FA-GRP-1144
  - TC-FA-GRP-1145
  - TC-FA-GRP-1146
coverage:
  web: automated
---

# Tab Users Kolom Group Role (Multi Role Node): Search per Kolom, Tier Mendahului Group Role, Filter Mencocokkan Setiap Pemegang Role, dan Search Hanya Teks Sel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control pada client Multi Role khusus (Pre-setup No 26; terpisah dari client utama Tabel A dan dari client TC-FA-GRP-937). Client dan akun disediakan tim FE, tidak tertulis di Pre-setup TC; password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis No 8 (Pre-setup tambahan, di-seed lewat API di hook `before`, dibersihkan di hook `after`; disediakan tim FE/BE tanpa endpoint karangan): node level 1 `Multi Role Node {runId}-164` (Assignable) dengan lima user subjek di bawah, dipakai bersama user Total Control, Default User, dan Read Only milik client Multi Role khusus (Pre-setup No 26) sehingga tabel Tab Users memuat tepat 8 baris; client ini hanya berisi user Tabel Dinamis No 8. Client juga punya Custom Field aktif Phone.

  | Kode | Email (fixture baru, ditetapkan tim FE) | Role | Sel kolom Group Role |
  |---|---|---|---|
  | U-GM | `Fixture.groupsTabUsers.uGm164.email` | tier Group Manager + Group Role Asset Admin di node | `Group Manager` |
  | U-2R | `Fixture.groupsTabUsers.u2r164.email` | Group Role Asset Admin + Asset Auditor | `2 roles` |
  | U-1R | `Fixture.groupsTabUsers.u1r164.email` | Group Role Asset Admin | `Asset Admin` |
  | U-AU | `Fixture.groupsTabUsers.uAu164.email` | Group Role Asset Auditor | `Asset Auditor` |
  | U-3R | `Fixture.groupsTabUsers.u3r164.email` | Group Role Asset Custodian + Asset Technician | `2 roles` |

- Password user subjek: `Spectra.env.FA_GRP_SUBJECT_PASSWORD` (env baru; didaftarkan di tempat yang sama dengan `FA_TC_PASSWORD`). Tidak ada login user subjek di spec ini.
- Pemulihan: user subjek dan node dihapus lewat API di hook `after` (tidak berasumsi seeding berhasil penuh).

## Test Steps

1. Klik angka Total User Multi Role Node

### TC-577: Search per kolom Group Role

2. Pastikan kolom Group Role tampil
3. Ketik Search `asset adm`, tekan Enter
4. Verifikasi baris U-1R (sel `Asset Admin`) tampil
5. Verifikasi baris lain tidak tampil
6. Ganti isi kotak search dengan `ASSET ADM`, tekan Enter
7. Verifikasi baris yang tampil identik dengan hasil huruf kecil (case-insensitive)
8. Ganti isi kotak search dengan string yang tidak ada di data, tekan Enter
9. Verifikasi empty state dengan ilustrasi, title "No results found", dan body "Try adjusting your search or filter."
10. Ganti isi kotak search dengan `Asset Technician`, tekan Enter
11. Verifikasi empty state dengan ilustrasi, title "No results found", dan body "Try adjusting your search or filter." (Search hanya mencocokkan teks yang tampil di sel, bukan nama role di dalam `[N] roles`; `Asset Technician` milik U-3R)
12. Klik `(←)` pada kotak Search

### TC-1144: Tier mendahului Group Role biasa

13. Verifikasi sel Group Role U-GM menampilkan `Group Manager` (bukan `Asset Admin` maupun `2 roles`)
14. Hover sel `2 roles` milik U-2R
15. Verifikasi tidak ada tooltip hover pada sel `2 roles` U-2R
16. Verifikasi sel Group Role U-3R menampilkan `2 roles`
17. Verifikasi sel Group Role U-1R menampilkan `Asset Admin`
18. Verifikasi sel Group Role user Total Control menampilkan `Total Control`
19. Verifikasi tabel memuat tepat 8 baris
20. Verifikasi tidak ada baris yang menampilkan `—` pada kolom Group Role

### TC-1145: Filter Group Role mencocokkan setiap pemegang role

21. Klik icon Filter
22. Buka dropdown Group Role
23. Verifikasi opsi Group Role memuat `Asset Admin` dan `Asset Auditor` (nama role di dalam sel `2 roles` tetap menjadi opsi)
24. Pilih Asset Admin pada Group Role, klik [Apply]
25. Verifikasi tepat tiga baris tampil: U-1R (sel `Asset Admin`), U-2R (sel `2 roles`), dan U-GM (sel `Group Manager`)
26. Verifikasi U-AU, U-3R, dan user client (Total Control, Default User, Read Only) tidak tampil
27. Buka Filter, ganti pilihan Group Role menjadi Asset Auditor, klik [Apply]
28. Verifikasi tepat U-AU dan U-2R tampil
29. Verifikasi U-GM, U-1R, U-3R, dan user client tidak tampil
30. Buka Filter, klik [Clear Field], klik [Apply]

### TC-1146: Search Group Role hanya mencocokkan teks sel

31. Ketik Search `Asset Admin`, tekan Enter
32. Verifikasi hanya U-1R tampil
33. Verifikasi U-2R, U-3R (sel `2 roles`), dan U-GM (sel `Group Manager`) tidak tampil walau memegang role Asset Admin
34. Ganti isi kotak search dengan `2 roles`, tekan Enter
35. Verifikasi tepat U-2R dan U-3R tampil
36. Ganti isi kotak search dengan `Group Manager`, tekan Enter
37. Verifikasi U-GM tampil
38. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): `(←)` pada kotak Search di akhir TC-577 dan TC-1146, dan membuka Filter lalu [Clear Field] dan [Apply] di akhir TC-1145 (mengosongkan filter sebelum TC berikutnya). Membuka dropdown Group Role pada TC-1145 dilakukan agar Expected a dapat diamati.
- Spec memiliki 38 langkah, di atas smell 35 langkah. Alasan: keempat TC memakai fixture Multi Role Node yang sama dan satu topik kolom Group Role Tab Users; fixture berat (lima user subjek) tidak perlu di-seed ulang, dan tiap blok berdiri sendiri.
- Temuan untuk QA:
  - Kode user subjek (U-GM, U-2R, ...) tidak punya email di TC; spec memakai fixture baru ditetapkan tim FE dan nama node bersuffix per run (S-12). Mekanisme memberi tier Group Manager dan Group Role pada node di-seed oleh tim FE/BE.
  - TC-1144 menyebut "tanpa tooltip hover" pada sel `[N] roles` tanpa langkah hover; spec menambah langkah hover sebagai langkah observasi.
  - TC-1145 tidak menyebut membuka dropdown sebelum memilih opsi; spec menambah langkah itu.

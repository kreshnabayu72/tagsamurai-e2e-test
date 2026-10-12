---
id: TC-GS-BRAND-E2E-015-create-validasi-diblokir
title: "Validasi Create Brand yang Diblokir"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-BRAND-42
  - TC-GS-BRAND-43
  - TC-GS-BRAND-45
  - TC-GS-BRAND-48
  - TC-GS-BRAND-52
  - TC-GS-BRAND-53
  - TC-GS-BRAND-54
coverage:
  web: automated
---

# Validasi Create Brand yang Diblokir

## Prerequisites

- Mode: FE+BE (backend nyata; TC-GS-BRAND-53 dan TC-GS-BRAND-54 butuh pengecekan keunikan nama ke backend).
- Akun aktor: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data pre-setup (brand tetap di Client A, tidak diubah spec): `Acme Corp` (dipakai TC-GS-BRAND-53) dan `Orion Tech` (dipakai TC-GS-BRAND-54) sebagai nama yang sudah ada.
- Data uji: semua nilai hanya diketik dan seluruh submit diblokir, sehingga tidak ada brand yang dibuat dan tidak ada seeding. Teks panjang dibangkitkan oleh skrip: 121 karakter huruf biasa (TC-GS-BRAND-45) dan 121 karakter huruf biasa yang diikuti emoji `🌟` diketik di akhir nilai (TC-GS-BRAND-52).
- Hook `afterEach`: tutup modal Create yang masih terbuka dan dirty lewat `[✕]`, lalu klik [Leave] pada dialog `Unsaved Changes`, kembali ke layar Brand (cadangan bila langkah 36 dan 37 tidak tercapai).
- Cleanup (hook `after`): bila ada brand tidak terduga yang terbentuk dengan nama dari spec ini (mis. `Star 🌟 Co`, `Star  Co`), hapus lewat API; tidak berasumsi langkah UI berhasil.
- Kemampuan teknis: pengetikan karakter per karakter dan paste via clipboard; penantian debounce ±500 ms; pembacaan nilai field dan jumlah karakter; pengecekan daftar Brand lewat API.
- State global: tidak ada yang diubah. Sesi sudah berada di akun default suite (Total Control Client A).

## Test Steps

### TC-GS-BRAND-42: Submit Create dengan Brand Name kosong

1. Buka Global Settings > Master Reference > Brand
2. Klik [+ Brand]
3. Klik [Submit] dengan field Brand Name kosong
4. Verifikasi error inline `Brand Name must not be empty` tampil
5. Verifikasi border field berwarna danger
6. Verifikasi record tidak dibuat
7. Verifikasi modal tetap terbuka

### TC-GS-BRAND-43: Submit Create dengan Brand Name hanya spasi

8. Ketik 3 spasi pada field Brand Name
9. Klik [Submit]
10. Verifikasi error inline `Brand Name must not be empty` tampil
11. Verifikasi record tidak dibuat

### TC-GS-BRAND-45: Create Brand Name 121 karakter

12. Klik [Clear Field]
13. Ketik Brand Name 121 karakter
14. Verifikasi karakter ke-121 masuk ke field (panjang nilai field 121 karakter)
15. Verifikasi error inline `Max. 120 characters` tampil saat mengetik
16. Klik [Submit]
17. Verifikasi submit diblokir
18. Verifikasi record tidak dibuat

### TC-GS-BRAND-48: Emoji diblok di level input pada field Brand Name (Create)

19. Klik [Clear Field]
20. Ketik `Star 🌟 Co`
21. Verifikasi karakter emoji tidak masuk ke field (nilai field tidak memuat `🌟`)
22. Verifikasi tidak ada pesan error karena emoji tidak pernah masuk field
23. Klik [Clear Field]
24. Tempel `🔥` ke field kosong
25. Verifikasi karakter emoji tidak masuk ke field (nilai field tetap kosong)
26. Verifikasi tidak ada pesan error karena emoji tidak pernah masuk field

### TC-GS-BRAND-52: Prioritas pesan Brand Name: panjang dan karakter sekaligus hanya menampilkan pesan panjang

27. Klik [Clear Field]
28. Ketik 121 karakter huruf biasa
29. Ketik `🌟` di akhir nilai
30. Verifikasi hanya error `Max. 120 characters` yang tampil
31. Verifikasi emoji `🌟` tidak masuk ke field (difilter di level input)
32. Verifikasi pesan `Brand Name contains invalid characters` tidak tampil

### TC-GS-BRAND-53: Cek keunikan real-time saat mengetik nama yang sudah ada dengan huruf berbeda

33. Klik [Clear Field]
34. Ketik `ACME CORP`
35. Berhenti mengetik ±500 ms
36. Verifikasi error inline `Brand Name already exists` muncul tanpa harus keluar dari field
37. Klik [Submit]
38. Verifikasi submit tidak membuat record

### TC-GS-BRAND-54: Duplikat dengan spasi tepi dideteksi setelah trim

39. Klik [Clear Field]
40. Ketik `  orion tech ` (2 spasi di depan, 1 spasi di belakang)
41. Tunggu ±500 ms
42. Verifikasi error inline `Brand Name already exists` tampil
43. Klik [Submit]
44. Verifikasi submit diblokir
45. Verifikasi tidak ada record baru: daftar Brand Client A lewat API tidak memuat brand bernama `ACME CORP`, `orion tech`, `Star 🌟 Co`, atau 121 karakter hasil uji

46. Klik `[✕]` untuk menutup form yang masih dirty
47. Verifikasi dialog `Unsaved Changes` tampil dengan body `You have unsaved changes. Are you sure you want to leave?`
48. Klik [Leave] pada dialog `Unsaved Changes` yang tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Seluruh validasi memakai satu pembukaan form (prinsip 3 dan 7 konvensi): validasi diblokir berurutan, tiap validasi diakhiri submit yang diblokir, dan pengecekan "tidak ada record" dilakukan sekali di langkah 45 lewat API karena tabel tertutup modal. Form ditutup di akhir spec (langkah 46 sampai 48).
- TC-GS-BRAND-52: emoji difilter di level input (TC-GS-BRAND-48), sehingga pesan `Brand Name contains invalid characters` tidak tampil; spec mengetik 121 karakter huruf biasa lalu `🌟` (langkah 27 sampai 32).
- Langkah 37 (Submit pada TC-GS-BRAND-53) dan 43 (Submit pada TC-GS-BRAND-54) menjalankan prinsip 7 (submit yang diblokir); TC-GS-BRAND-54 sumber hanya meminta error inline.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 12, 19, 23, 27, 33, dan 39 (`[Clear Field]` untuk mengosongkan field Brand Name sebelum nilai uji berikutnya; Clear Field tidak membuat dialog menurut FI-01 dan tidak membuat record), serta langkah 46 dan 48 (menutup form dirty lewat `[✕]` dan [Leave]; langkah 47 memverifikasi dialog `Unsaved Changes`).

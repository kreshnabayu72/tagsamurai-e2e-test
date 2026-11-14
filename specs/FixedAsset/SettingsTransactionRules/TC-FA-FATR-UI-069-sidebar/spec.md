---
id: TC-FA-FATR-UI-069-sidebar
title: "Sidebar Category Tree: pohon, pencarian, dan collapse"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - §4.1#r4
  - §4.1#p1
  - §4.1#b1
  - §4.1#b5
  - §4.1#b6
  - §4.1#r13
  - §4.1#r14
  - §4.1#r15
  - §4.3#r18
  - §4.4#r1
  - §4.5#b3
  - §4.5#b5
  - S-11
  - §9.5#r12
  - §9.5#r18
  - EB-SRC-6@sidebar-category-tree
smoke: []
dependsOn: []
trace:
  §4.1#r4: [2, 7]
  §4.1#p1: [6, 30, 35]
  §4.1#b1: [3, 4]
  §4.1#b5: [23, 25, 30, 31]
  §4.1#b6: [38, 39, 41]
  §4.1#r13: [11, 16, 20]
  §4.1#r14: [10, 13]
  §4.1#r15: [18, 20]
  §4.3#r18: [38, 39]
  §4.4#r1: [10, 11, 13]
  §4.5#b3: [47, 50, 52, 54]
  §4.5#b5: [43, 45]
  S-11: 35
  §9.5#r12: 5
  §9.5#r18: [16, 18]
  EB-SRC-6@sidebar-category-tree: [28, 30]
anchor: []
coverage:
  web: automated
---

# Sidebar Category Tree: pohon, pencarian, dan collapse

## Prerequisites
- Aktor: Total Control.
- Layar awal: Sidebar Category Tree pada halaman Transaction Settings.
- Komponen: Sidebar Category Tree
- Data:
  - DU-069-1: Pohon Category: item teratas `All categories`, lalu induk `Vehicle` dengan Category leaf `Pool car` dan `Delivery van`, serta Category leaf `Machinery`.
  - DU-069-2: Kata kunci pencarian yang dicoba: `Pool` (cocok dengan `Pool car`) dan `Truck` (tidak cocok dengan Category mana pun).
- Kondisi:
  - K1: halaman dibuka pertama kali pada layar selebar desktop, pohon memakai DU-069-1, sidebar terbuka.
  - K2: sidebar terbuka, pohon memakai DU-069-1, cabang `Vehicle` tertutup, `All categories` terpilih.
  - K3: sidebar terbuka, pohon memakai DU-069-1, kolom pencarian kosong.
  - K4: layar di bawah breakpoint tablet, pohon memakai DU-069-1.
  - K5: sidebar terbuka, pohon memakai DU-069-1, fokus keyboard berada di baris `All categories` pada pohon.

## Test Steps

### Isi awal pohon
1. Tampilkan Sidebar Category Tree dengan kondisi K1
2. Verifikasi Category Tree tampil di sisi kanan halaman
3. Verifikasi item teratas pohon adalah `All categories`
4. Verifikasi pohon Category `Vehicle` dan `Machinery` tampil di bawah `All categories`
5. Verifikasi `All categories` terpilih dan terbuka
6. Verifikasi kolom pencarian tampil dengan placeholder `Search category...`
7. Verifikasi tombol Expand/Collapse All tampil di samping kolom pencarian

### Klik Category induk hanya membuka cabang
8. Tampilkan Sidebar Category Tree dengan kondisi K2
9. Klik `Vehicle`
10. Verifikasi cabang `Vehicle` terbuka dan menampilkan `Pool car` dan `Delivery van`
11. Verifikasi `All categories` masih menjadi node terpilih setelah `Vehicle` diklik
12. Klik `Vehicle` sekali lagi
13. Verifikasi cabang `Vehicle` tertutup

### Hanya All categories dan Category leaf yang dapat dipilih
14. Tampilkan Sidebar Category Tree dengan kondisi K2
15. Klik `Machinery`
16. Verifikasi `Machinery` terpilih
17. Klik `Vehicle`
18. Verifikasi `Vehicle` hanya membuka cabangnya dan tidak menjadi node terpilih, sehingga pilihan hanya ada pada `All categories` dan Category leaf
19. Klik `Pool car`
20. Verifikasi `Pool car` terpilih sebagai tingkat tempat aturan diatur

### Expand All dan Collapse All
21. Tampilkan Sidebar Category Tree dengan kondisi K2
22. Klik tombol Expand/Collapse All
23. Verifikasi semua cabang terbuka sehingga `Pool car` dan `Delivery van` tampil
24. Klik tombol Expand/Collapse All sekali lagi
25. Verifikasi cabang `Vehicle` tertutup kembali

### Pencarian berjalan saat Enter dan menyisakan induk
26. Tampilkan Sidebar Category Tree dengan kondisi K3
27. Ketik `Pool` pada kolom pencarian tanpa menekan Enter
28. Verifikasi daftar Category masih menampilkan `Vehicle` dan `Machinery` selama Enter belum ditekan
29. Tekan Enter pada kolom pencarian
30. Verifikasi `Vehicle` tampil bersama turunannya `Pool car`
31. Verifikasi `Machinery` dan `Delivery van` tidak ada pada hasil pencarian

### Pencarian tanpa hasil
32. Tampilkan Sidebar Category Tree dengan kondisi K3
33. Ketik `Truck` pada kolom pencarian
34. Tekan Enter pada kolom pencarian
35. Verifikasi teks `No categories found` tampil pada Category Tree

### Collapse dan buka kembali
36. Tampilkan Sidebar Category Tree dengan kondisi K1
37. Klik tombol dengan label `Collapse Category Tree`
38. Verifikasi tombol kecil dengan label `Open Category Tree` tampil di kanan atas
39. Verifikasi pohon Category tidak tampil selama Category Tree collapsed
40. Klik tombol dengan label `Open Category Tree`
41. Verifikasi pohon Category tampil kembali dengan `All categories` di bagian teratas

### Layar di bawah breakpoint tablet
42. Tampilkan Sidebar Category Tree dengan kondisi K4
43. Verifikasi Category Tree tampil collapsed dengan tombol kecil berlabel `Open Category Tree`
44. Klik tombol dengan label `Open Category Tree`
45. Verifikasi pohon Category terbuka lewat tombol pembukanya

### Navigasi keyboard dan atribut ARIA tree
46. Tampilkan Sidebar Category Tree dengan kondisi K5
47. Verifikasi pohon Category memiliki peran `tree`
48. Tekan ArrowDown sampai fokus berada di baris `Vehicle`
49. Tekan ArrowRight
50. Verifikasi cabang `Vehicle` terbuka
51. Tekan ArrowDown
52. Verifikasi fokus berpindah ke baris `Pool car`
53. Tekan ArrowLeft
54. Verifikasi fokus kembali ke baris `Vehicle`

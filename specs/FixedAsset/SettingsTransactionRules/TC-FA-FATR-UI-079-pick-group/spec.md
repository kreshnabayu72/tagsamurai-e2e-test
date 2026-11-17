---
id: TC-FA-FATR-UI-079-pick-group
title: "Dialog Select Group: tree picker dan validasi"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules:
  - "§4.1#r12"
  - "§4.1#p1"
  - "§4.1#r409"
  - "§4.5#b4"
  - "§6#r12"
  - "§7#r17"
  - "D-03"
  - "S-08"
smoke: []
dependsOn: []
trace:
  §4.1#r12: [2, 4, 9, 26]
  §4.1#p1: [2, 3, 15, 16]
  §4.1#r409: [29, 30, 32]
  §4.5#b4: [35, 37]
  §6#r12: 30
  §7#r17: [39, 40]
  D-03: [4, 5, 9, 10, 12, 15, 19, 22]
  S-08: [43, 44]
anchor: []
coverage:
  web: automated
---

# Dialog Select Group: tree picker dan validasi

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Transaction Settings, Dialog Add override - Borrow dengan Scope `Group`; Dialog Select Group dibuka dari tombol `[Select Group]`.
- Komponen: Dialog Select Group
- Data:
  - DU-079-1: Group `Proyek Karawang`, node tingkat atas di tree, dengan turunan `Workshop`.
  - DU-079-2: Group `Proyek Bekasi`, node tingkat atas di tree.
  - DU-079-3: kata kunci Search `Workshop`.
  - DU-079-4: kata kunci Search `Zebra Tidak Ada`, tidak cocok dengan node mana pun.
- Kondisi:
  - K1: tree hanya memuat node tingkat atas DU-079-1 dan DU-079-2 untuk aktor yang melihat semua Group; belum ada Group terpilih.
  - K2: tidak ada Group dalam cakupan aktor.

## Test Steps

### Judul, pencarian, footer, dan sifat tree multi-select
1. Tampilkan Dialog Select Group dengan kondisi K1
2. Verifikasi judul dialog `Select Group`
3. Verifikasi kotak pencarian memuat placeholder `Search group...`
4. Verifikasi dialog tampil sebagai modal dengan tree Group yang memuat `Proyek Karawang` dan `Proyek Bekasi`, tiap node memiliki checkbox
5. Verifikasi footer memuat tombol `Cancel` dan `Select`

### Memilih parent mencakup turunannya
6. Tampilkan Dialog Select Group dengan kondisi K1
7. Perluas node `Proyek Karawang`
8. Centang node `Proyek Karawang`
9. Verifikasi node `Workshop` ikut tercentang
10. Verifikasi node `Proyek Bekasi` tidak tercentang
11. Hilangkan centang node `Proyek Karawang`
12. Verifikasi node `Workshop` ikut tidak tercentang

### Pencarian node
13. Tampilkan Dialog Select Group dengan kondisi K1
14. Ketik Search `Workshop` pada kotak pencarian
15. Verifikasi tree menampilkan `Workshop` beserta parent-nya `Proyek Karawang`
16. Verifikasi node `Proyek Bekasi` tidak tampil

### Pilihan sementara dibuang saat Cancel dan dialog dibuka ulang
17. Tampilkan Dialog Select Group dengan kondisi K1
18. Centang node `Proyek Bekasi`
19. Verifikasi node `Proyek Bekasi` tercentang
20. Klik `[Cancel]`
21. Tampilkan Dialog Select Group dengan kondisi K1
22. Verifikasi node `Proyek Bekasi` tidak tercentang

### Select dengan pilihan
23. Tampilkan Dialog Select Group dengan kondisi K1
24. Centang node `Proyek Bekasi`
25. Klik `[Select]`
26. Verifikasi dialog Select Group tertutup dan badge `Proyek Bekasi` tampil di bawah tombol `Select Group` pada Dialog Add override

### Select tanpa pilihan
27. Tampilkan Dialog Select Group dengan kondisi K1
28. Klik `[Select]`
29. Verifikasi dialog Select Group tetap terbuka
30. Verifikasi pesan `You must make a selection` tampil di footer dialog
31. Centang node `Proyek Bekasi`
32. Verifikasi pesan `You must make a selection` hilang

### Menutup dialog
33. Tampilkan Dialog Select Group dengan kondisi K1
34. Klik backdrop di luar dialog
35. Verifikasi dialog Select Group tetap terbuka
36. Tekan `Esc`
37. Verifikasi dialog Select Group tertutup

### Empty state tidak ada Group dalam cakupan aktor
38. Tampilkan Dialog Select Group dengan kondisi K2
39. Verifikasi judul empty state `No group yet` tampil
40. Verifikasi deskripsi `Get started by creating your first group.` tampil

### Empty state hasil pencarian tanpa hasil
41. Tampilkan Dialog Select Group dengan kondisi K1
42. Ketik Search `Zebra Tidak Ada` pada kotak pencarian
43. Verifikasi judul empty state `No results found` tampil pada tree Select Group
44. Verifikasi deskripsi empty state `Try adjusting your search or filter.` tampil pada tree Select Group

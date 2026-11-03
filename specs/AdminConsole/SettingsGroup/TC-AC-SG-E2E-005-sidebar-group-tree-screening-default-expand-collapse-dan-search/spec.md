---
id: TC-AC-SG-E2E-005-sidebar-group-tree-screening-default-expand-collapse-dan-search
title: "Sidebar Group Tree: Screening, Default, Expand/Collapse, dan Search"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-15
  - TC-AC-SG-16
  - TC-AC-SG-18
  - TC-AC-SG-19
  - TC-AC-SG-20
coverage:
  web: automated
---

# Sidebar Group Tree: Screening, Default, Expand/Collapse, dan Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-group` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak diubah): `Pohon Uji Utama` entitas Principal (#16, 14 group); agregat "Total User: 10" dan "Total Member: 12" (#17, #19).
- Data Dinamis: tidak ada; spec tidak membuat atau mengubah data sehingga tidak ada seeding, suffix `{runId}-005`, maupun cleanup.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-15: Screening Sidebar Group Tree

1. Susuri Sidebar Group Tree dari atas ke bawah
2. Verifikasi Title "Groups" pada header sidebar
3. Verifikasi header sidebar tanpa tombol close dan tanpa garis pemisah
4. Verifikasi Subtitle "Select a group to filter the table."
5. Verifikasi input pencarian always-open dengan placeholder "Search groups..."
6. Verifikasi tombol ikon-saja Expand/Collapse All sejajar dengan input pencarian
7. Verifikasi tombol `[+] Group` (teks, severity primary) rata kanan dengan ikon `+` di kiri label "Group"
8. Verifikasi root "All Groups (14)" aktif (highlight dan bold) di atas seluruh group yang ter-expand
9. Hover tombol Expand/Collapse All
10. Hover tombol toggle mengambang di tepi panel
11. Verifikasi tooltip tombol toggle "Collapse Group Tree" pada state Open

### TC-AC-SG-16: Default sidebar: All Groups aktif dan seluruh tree ter-expand

12. Perhatikan state tree tanpa mengklik apa pun
13. Verifikasi root "All Groups" aktif
14. Verifikasi seluruh node level 1 sampai `Room 301` terlihat (tree ter-expand penuh)
15. Verifikasi tabel menampilkan seluruh 14 group tanpa filter

### TC-AC-SG-18: Tombol Expand/Collapse All pada sidebar

16. Klik tombol Expand/Collapse All sekali
17. Verifikasi seluruh tree ter-collapse sehingga hanya group level 1 yang terlihat
18. Klik tombol Expand/Collapse All lagi
19. Verifikasi seluruh tree ter-expand sehingga `Room 301` terlihat kembali
20. Klik tanda panah node `Region A` untuk meng-collapse hanya node itu
21. Verifikasi `Branch 1`, `Branch 2`, `Floor 1`, dan `Room 301` tersembunyi
22. Verifikasi pilihan node tidak berubah (`All Groups` tetap aktif)
23. Klik tanda panah node `Region A` untuk meng-expand kembali

### TC-AC-SG-19: Search sidebar tree tidak case-sensitive dan meng-expand ke node yang cocok

24. Klik tombol Expand/Collapse All untuk meng-collapse tree
25. Ketik "room 301" pada input "Search groups..."
26. Verifikasi pencarian "room 301" meng-expand `Region A`, `Branch 1`, dan `Floor 1`
27. Verifikasi node `Room 301` terlihat dan ter-highlight
28. Verifikasi node yang tidak cocok (`Region B`, `Head Office`) tetap terlihat
29. Ganti isi input pencarian dengan "ROOM"
30. Verifikasi hasil pencarian "ROOM" sama dengan hasil "room 301" (substring, tidak case-sensitive)
31. Ganti isi input pencarian dengan "oom 30"
32. Verifikasi hasil pencarian "oom 30" sama dengan hasil "room 301" (substring di tengah nama)
33. Verifikasi node terpilih `All Groups` tidak berubah
34. Verifikasi isi tabel tetap 14 group
35. Verifikasi Group Context Header tetap "Total User: 10" dan "Total Member: 12"

### TC-AC-SG-20: Search sidebar tanpa hasil menampilkan empty state standar

36. Klik ikon clear pada input pencarian
37. Ketik "zzzxxx" pada input "Search groups..."
38. Verifikasi area tree menampilkan empty state standar dengan Title "No results found" dan Description "Try adjusting your search or filter."
39. Klik ikon clear pada input pencarian

## Notes

- Ukuran spec (39 langkah, sedikit di atas smell sekitar 35 langkah): satu komponen (Sidebar Group Tree) pada satu halaman, seluruhnya baca-saja, dan tiap blok TC dimulai dari keadaan tree yang dipulihkan langkah penghubung sehingga berdiri sendiri; klausa Expected tiap TC menjadi `Verifikasi` sendiri (S-01).
- Langkah penghubung (S-03, S-09): langkah 1 dan 12 mengamati tanpa asersi sendiri; langkah 23 meng-expand kembali `Region A` sebelum TC-AC-SG-19; langkah 36 dan 39 mengosongkan pencarian sidebar; pada akhir TC-AC-SG-19 tree masih ter-collapse dan hasil pencarian "oom 30" aktif, lalu dibersihkan langkah 36.
- Pencarian sidebar tree diketik tanpa Enter (sesuai TC); aturan Search tabel (Enter) tidak berlaku untuk input ini.
- Temuan untuk QA:
  - TC-AC-SG-15 langkah 3 (hover tombol Expand/Collapse All) tidak punya Expected padanan; spec menuliskannya sebagai aksi tanpa asersi (langkah 9).
  - TC-AC-SG-19 Expected a menyebut node yang tidak cocok "tetap terlihat" tanpa menyebut apakah node itu ter-collapse atau ter-expand; spec hanya mengasersi bahwa `Region B` dan `Head Office` terlihat.

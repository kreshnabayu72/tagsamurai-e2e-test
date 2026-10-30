---
id: TC-GS-UOM-E2E-044-state-hover-fokus-backdrop-modal-dan-focus-trap
title: "State Hover dan Fokus Komponen, Backdrop Tidak Menutup Modal, dan Focus Trap Modal Edit, Detail, Delete"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-259
  - TC-GS-UOM-298
  - TC-GS-UOM-299
coverage:
  web: automated
---

# State Hover dan Fokus Komponen, Backdrop Tidak Menutup Modal, dan Focus Trap Modal Edit, Detail, Delete

## Prerequisites

- Mode: FE+BE. Suite berjalan serial (`parallel: false`, lihat `suite.md`).
- Flag Guided Tooltip halaman Measurement mengikuti pernyataan hook suite di `suite.md`.
- Fixture: `fixtures/measurement.json` belum ada; tim FE menyiapkannya (lihat `suite.md`, bagian Data bersama).
- Akun: Total Control Client A, Sari Dewi (Sari D), `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > Master Reference > Measurement dilakukan sekali di hook `before` suite.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (hanya dibaca; Last Updated lebih lama dari hari uji): Box / box (Used By (Items) 4), Dozen / dz (2), Gram / g (1), Kilogram / kg (1), Liter / L (0), Meter / m (0), Pack / pk (0), Pieces / pc (3).
- Data Dinamis: tidak ada; spec tidak men-seed data dan tidak membuat unit.
- Spec tidak mengubah data unit. Baris Pre-setup Liter, Meter, dan Pieces hanya dibuka, dibatalkan, atau ditutup tanpa perubahan (Last Updated tidak berubah; pengecualian S-06): Liter pada modal Edit ditutup lewat `[✕]` tanpa mengubah field, Meter pada dialog Delete hanya dibatalkan (`[Cancel]`), Pieces hanya dibaca di Modal Unit Detail (Item Type List: FAMS Laptop, Monitor; Supply Printer Ink).
- Modal Changelog Measurement memuat sedikitnya satu entri (Pre-setup menghasilkan entri Create).
- State global yang dipulihkan: seleksi baris dikosongkan di langkah spec (hook `after` sebagai cadangan); Modal dan dialog ditutup di hook `beforeEach`.
- Hook `beforeEach`: buka Global Settings > Master Reference > Measurement.
- Kemampuan teknis: navigasi keyboard (Tab berulang) dengan pembacaan elemen aktif (`document.activeElement`); hover; pembacaan state visual (latar hover dan terpilih, ring fokus, border, rotasi chevron) lewat gaya terhitung atau atribut state komponen; klik pada area backdrop di luar modal.

## Test Steps

### TC-GS-UOM-298: State hover dan fokus komponen tabel, tombol [+ Unit], input form, dan accordion

1. Arahkan kursor ke baris Box
2. Verifikasi baris Box menampilkan latar hover
3. Centang checkbox baris Box
4. Verifikasi baris Box menampilkan latar terpilih
5. Tekan Tab hingga fokus berada di `[+ Unit]`
6. Verifikasi tombol `[+ Unit]` menampilkan ring fokus saat difokuskan keyboard
7. Arahkan kursor ke tombol `[+ Unit]`
8. Verifikasi tombol `[+ Unit]` menampilkan hover filled primary
9. Klik `[+ Unit]`
10. Arahkan kursor ke field Unit Name
11. Verifikasi input Unit Name menampilkan border `severity="primary"` saat hover
12. Fokuskan field Unit Name
13. Verifikasi input Unit Name menampilkan ring fokus `severity="primary"` saat fokus
14. Tutup form lewat `[✕]`
15. Hapus centang baris Box
16. Ketik Search `Pieces`, tekan Enter
17. Buka Detail Pieces (klik link Unit Name `Pieces`)
18. Arahkan kursor ke header Accordion `Item Type List`
19. Verifikasi header Accordion menampilkan latar hover
20. Klik header Accordion `Item Type List` untuk collapse
21. Verifikasi chevron berputar saat collapse
22. Klik header Accordion `Item Type List` untuk expand
23. Verifikasi chevron berputar saat expand
24. Tutup Modal Unit Detail lewat `[✕]`
25. Klik `(←)` pada kotak Search

### TC-GS-UOM-259: Focus trap pada modal Edit, Unit Detail, dan dialog Delete

26. Klik `⋯` baris Liter, pilih Edit
27. Tekan Tab berulang melewati elemen terakhir modal Edit
28. Verifikasi fokus keyboard tetap berputar di dalam modal Edit
29. Verifikasi fokus tidak berpindah ke tabel
30. Verifikasi fokus tidak berpindah ke Tab di belakang modal Edit
31. Tutup modal Edit lewat `[✕]`
32. Ketik Search `Pieces`, tekan Enter
33. Buka Detail Pieces (klik link Unit Name `Pieces`)
34. Tekan Tab berulang melewati elemen terakhir Modal Unit Detail
35. Verifikasi fokus keyboard tetap berputar di dalam Modal Unit Detail
36. Verifikasi fokus tidak berpindah ke tabel
37. Verifikasi fokus tidak berpindah ke Tab di belakang Modal Unit Detail
38. Tutup Modal Unit Detail lewat `[✕]`
39. Klik `(←)` pada kotak Search
40. Klik `⋯` baris Meter, pilih Delete
41. Tekan Tab berulang melewati tombol terakhir dialog Delete
42. Verifikasi fokus keyboard tetap berputar di dalam dialog Delete
43. Verifikasi fokus tidak berpindah ke tabel
44. Verifikasi fokus tidak berpindah ke Tab di belakang dialog Delete
45. Klik [Cancel]

### TC-GS-UOM-299: Klik backdrop tidak menutup Modal Changelog, Unit Detail, dan dialog Delete

46. Klik Changelog
47. Klik area backdrop di luar Modal Changelog
48. Verifikasi Modal Changelog tetap terbuka
49. Tutup Modal Changelog lewat `[✕]`
50. Verifikasi Modal Changelog tertutup
51. Ketik Search `Pieces`, tekan Enter
52. Buka Detail Pieces (klik link Unit Name `Pieces`)
53. Klik area backdrop di luar Modal Unit Detail
54. Verifikasi Modal Unit Detail tetap terbuka
55. Tutup Modal Unit Detail lewat `[✕]`
56. Verifikasi Modal Unit Detail tertutup
57. Klik `(←)` pada kotak Search
58. Klik `⋯` baris Meter, pilih Delete
59. Klik area backdrop di luar dialog Delete
60. Verifikasi dialog `Delete Unit` tetap terbuka
61. Klik [Cancel]
62. Verifikasi dialog `Delete Unit` tertutup
63. Verifikasi baris Meter masih tampil di tabel (tidak terhapus)

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (63). Alasan: tiga TC a11y UI-only berkelas sama (state komponen, focus trap, backdrop) pada layar yang sama, tanpa mengubah data; tiap blok membuka dan menutup modal sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC dalam spec: 298, 259, 299 (urutan sumber 259, 298, 299). TC-GS-UOM-298 lebih dulu karena menyentuh seleksi baris dan Create yang dibersihkan di akhir blok.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 15 (menghapus centang baris Box sebelum Search `Pieces`); langkah 16, 32, dan 51 (Search `Pieces`) serta langkah 25, 39, dan 57 (`(←)` pada kotak Search): baris `Pieces` berada di halaman 2 pada tabel baseline 20 unit suite (S-14); langkah 14 dan 24 adalah penutupan form dan modal sesuai TC. Form Create pada TC-GS-UOM-298 tidak diisi, sehingga penutupan lewat `[✕]` tidak memunculkan dialog `Unsaved Changes` (form Create kosong tidak dirty).
- TC-GS-UOM-259 membuka modal Edit baris Liter dan dialog Delete baris Meter; keduanya Pre-setup tanpa relasi, hanya dibuka dan dibatalkan (S-06, pengecualian).
- Semua TC sumber spec ini dikerjakan di sini; tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-UOM-298: Expected membahas gaya visual (latar, border, ring fokus, rotasi chevron) tanpa nilai konkret (warna atau class); spec mengasersi keberadaan state sesuai teks Expected, nilai konkret perlu disepakati QA/FE saat script.
  - TC-GS-UOM-299 butir d menyebut modal tertutup lewat `[✕]`, `Esc`, ataupun tombol dialog, tetapi langkah TC hanya memakai `[✕]` dan `[Cancel]`; `Esc` tidak diuji.
  - TC-GS-UOM-259 tidak menyebut apakah modal Edit yang ditutup tanpa perubahan memunculkan dialog `Unsaved Changes`; spec mengasumsikan modal Edit tanpa perubahan field tertutup tanpa dialog.

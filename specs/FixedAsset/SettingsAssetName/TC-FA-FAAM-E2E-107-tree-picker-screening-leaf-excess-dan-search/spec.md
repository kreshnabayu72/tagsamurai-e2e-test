---
id: TC-FA-FAAM-E2E-107-tree-picker-screening-leaf-excess-dan-search
title: "Tree Picker: Screening, Hanya Leaf Dipilih, Node Excess, dan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-318
  - TC-FA-FAAM-319
  - TC-FA-FAAM-320
  - TC-FA-FAAM-321
  - TC-FA-FAAM-322
coverage:
  web: automated
---

# Tree Picker: Screening, Hanya Leaf Dipilih, Node Excess, dan Search

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya; suite berjalan serial (`parallel: false`). Spec ini tidak memakai seed API per TC.
- Data Pre-setup #22 yang hanya dibaca: pohon kategori Electronics (Laptop, Phone), IT Equipment, Logistics, Office Furniture, Office Equipment, Vehicles, dan Legacy Category (excess). Form Create hanya dibuka untuk mengakses Tree Picker dan tidak pernah disimpan; tidak ada record yang dibuat.
- Kemampuan teknis: tidak ada tambahan di luar `suite.md`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-318: Screening Modal Tree Picker

1. Klik `[+ Asset Name]`
2. Klik `[Select Category]`
3. Verifikasi Title `Select Category`
4. Verifikasi komponen TreeSelect single-select tampil
5. Verifikasi Search dengan placeholder `Search category` tampil di atas tree
6. Verifikasi footer memuat tombol `[Select]` dan `[Cancel]`
7. Verifikasi tombol `[Select]` nonaktif sebelum leaf dipilih
8. Verifikasi node berurutan A→Z pada tiap level
9. Verifikasi `Electronics` tampil sebagai parent non-selectable

### TC-FA-FAAM-320: Node excess dari kategori tidak dapat dipilih

10. Klik node `Legacy Category`
11. Verifikasi node `Legacy Category` tidak terpilih
12. Verifikasi tombol `[Select]` tetap nonaktif

### TC-FA-FAAM-319: Hanya node leaf dapat dipilih dan Select aktif setelah leaf dipilih

13. Klik node `Electronics`
14. Verifikasi klik `Electronics` (internal) tidak memilih apa pun dan tombol `[Select]` tetap nonaktif
15. Klik node `Laptop`
16. Verifikasi node `Laptop` tersorot
17. Verifikasi tombol `[Select]` aktif

### TC-FA-FAAM-321: Search mencocokkan nama node di semua level dan menampilkan ancestor ter-expand

18. Ketik `lap` di Search
19. Verifikasi node `Laptop` tampil
20. Verifikasi ancestor `Electronics` tampil ter-expand
21. Klik ancestor `Electronics`
22. Verifikasi ancestor non-match `Electronics` yang internal tidak terpilih
23. Verifikasi `lap` (huruf kecil) mencocokkan `Laptop` sebagai substring tanpa membedakan huruf besar-kecil

### TC-FA-FAAM-322: Search tanpa hasil menampilkan empty state pencarian

24. Ganti isi kotak Search dengan `zzzz`
25. Verifikasi empty state Title `No results found` dan Description `Try adjusting your search or filter.` tampil
26. Klik `[Cancel]`
27. Klik `[✕]` pada modal Create

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): `[Cancel]` menutup Tree Picker dan `[✕]` menutup modal Create yang tidak dirty sehingga dialog Unsaved Changes tidak muncul (langkah 26, 27).
- Urutan TC di dalam spec: TC-FA-FAAM-318, TC-FA-FAAM-320, TC-FA-FAAM-319, TC-FA-FAAM-321, lalu TC-FA-FAAM-322. TC-FA-FAAM-320 dijalankan sebelum TC-FA-FAAM-319 karena TC-FA-FAAM-320 mensyaratkan tidak ada leaf terpilih (`[Select]` nonaktif) sedangkan TC-FA-FAAM-319 menyorot `Laptop` dan tidak punya langkah pembersih.
- Modal Create dan Tree Picker dibuka satu kali untuk lima TC tanpa submit (bagian 3, halaman yang sama dipakai berulang).
- Temuan untuk QA:
  - TC-FA-FAAM-318 Precondition menyebut pohon Pre-setup #22 tanpa `Office Equipment` dan `Vehicles` (hanya lima akar), sedangkan Pre-setup #22 memuat tujuh akar; spec tidak mengasersi daftar akar lengkap pada TC ini.
  - TC-FA-FAAM-318 Expected f ("`Electronics` sebagai parent non-selectable") tidak menyebut indikator tampilannya; spec mengasersi node tampil sebagai parent dan perilaku non-selectable diasersi pada langkah 14.
  - TC-FA-FAAM-321 Expected b ("Ancestor non-match tidak dapat dipilih bila internal") tidak punya langkah pemicu di TC; spec menambah langkah klik ancestor (langkah 21).
  - TC-FA-FAAM-321 Expected c dan judul menyebut pencarian "semua level"; spec hanya menguji `lap` yang cocok pada level anak.

---
id: TC-FA-CAT-E2E-008-walkthrough-saat-sidebar-collapsed-atau-terbuka
title: "Walkthrough dengan Sidebar Collapsed dan Terbuka (Desktop)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAT-644
  - TC-FA-CAT-639
  - TC-FA-CAT-641
  - TC-FA-CAT-643
coverage:
  web: automated
---

# Walkthrough dengan Sidebar Collapsed dan Terbuka (Desktop)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data: client CatMain (Pre-setup #20, plan Enterprise): 15 kategori; L1 `Accessory`, `Default Category`, `Electronics` (anak `Laptop`, `Monitor`), `Furniture`, `Peripheral` (anak `Keyboard`, `Mouse`), `Spare Part`, `Tools`, `Vehicle`.
- State awal: flag `guided_tooltip_seen_fa-settings-categories` bernilai true (precondition TC; diatur hook suite `before` dan dipulihkan `after`). Preferensi Open/Collapsed sidebar halaman Categories dihapus di hook `before` dan `after` (kemampuan disediakan tim FE); sidebar dimulai dalam keadaan terbuka.
- Varian penutupan walkthrough (TC-FA-CAT-641):
  | Varian | Cara menutup walkthrough |
  |---|---|
  | Done | Klik `[Next]` sampai step terakhir lalu klik `[Done]` |
  | Skip | Klik `[Skip]` pada Step 1 |
  | Overlay | Klik overlay gelap pada Step 1 |
  
- Kemampuan teknis: menekan F5 dan berpindah menu.
- Seed dan pemulihan client Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-categories.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-644: Walkthrough dimulai saat sidebar sudah terbuka: keadaan sidebar tidak berubah selama dan setelah tur

1. Pastikan sidebar terbuka lalu klik `[?]`
2. Verifikasi sidebar tetap terbuka selama Step 1 tanpa perubahan keadaan
3. Verifikasi Step 1 menyorot Sidebar Category Tree dengan Title `Category Tree` dan Description `Use this tree to navigate the category hierarchy and add new categories.`
4. Klik `[Next]` sampai step terakhir lalu klik `[Done]`
5. Verifikasi sidebar tetap terbuka setelah tur selesai
6. Tekan F5
7. Verifikasi sidebar terbuka (preferensi collapse tersimpan tidak berubah)

### TC-FA-CAT-639: Walkthrough dimulai saat sidebar collapsed (desktop): sidebar dibuka otomatis selama Step 1 dan Step 1 tidak dilewati

8. Klik Floating Toggle di tepi kiri panel sidebar sehingga sidebar collapsed
9. Klik tombol `[?]` di sebelah kanan Breadcrumb
10. Verifikasi sidebar terbuka otomatis sehingga target Sidebar Category Tree terlihat
11. Verifikasi walkthrough dimulai dari Step 1 (tidak dilewati ke Step 2) dengan indikator `Step 1 of 3`
12. Verifikasi Step 1 menyorot Sidebar Category Tree dengan Title `Category Tree` dan Description `Use this tree to navigate the category hierarchy and add new categories.`
13. Verifikasi penomor step tidak berubah akibat pembukaan sidebar (tetap `Step 1 of 3`)
14. Klik `[Skip]`

### TC-FA-CAT-641: Setelah walkthrough selesai, di-skip, atau ditutup, sidebar kembali collapsed (desktop)

15. Klik Floating Toggle untuk membuka sidebar
16. Klik Floating Toggle di tepi kiri panel sidebar sehingga sidebar collapsed
17. Klik `[?]`
18. Tutup walkthrough sesuai kolom "Cara menutup walkthrough" pada tabel Varian penutupan
19. Verifikasi walkthrough berakhir
20. Hover Floating Toggle
21. Verifikasi Floating Toggle berada di tepi kanan layar dengan tooltip `Open Category Tree`
22. Verifikasi panel sidebar tersembunyi (tidak tertinggal terbuka setelah tur)

### TC-FA-CAT-643: Preferensi collapse sidebar tersimpan user tidak berubah oleh walkthrough

23. Klik Floating Toggle untuk membuka sidebar
24. Klik Floating Toggle di tepi kiri panel sidebar sehingga sidebar collapsed
25. Klik `[?]` lalu selesaikan walkthrough sampai `[Done]`
26. Verifikasi preferensi tersimpan tetap collapsed (sidebar collapsed meski sempat dibuka otomatis selama Step 1)
27. Tekan F5
28. Verifikasi sidebar tetap collapsed setelah F5
29. Buka menu lain lalu kembali ke Fixed Asset > Settings > Categories
30. Verifikasi sidebar tetap collapsed setelah kembali dari menu lain
31. Klik Floating Toggle untuk membuka sidebar

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Urutan (S-10): TC-FA-CAT-644 (sidebar terbuka sejak awal) mendahului TC-FA-CAT-639, 641, dan 643 yang membutuhkan sidebar collapsed; urutan akhir TC-FA-CAT-644, 639, 641, 643.
- Langkah penghubung (S-03): langkah 6 (F5 untuk mengamati preferensi), langkah 14 (menutup walkthrough TC-FA-CAT-639 dengan `[Skip]`, yang mengembalikan sidebar ke collapsed), langkah 15 dan 23 (membuka sidebar agar langkah pertama TC dapat meng-collapse-nya), langkah 31 (mengembalikan sidebar terbuka).
- Langkah berulang (bagian 8b butir 7): untuk setiap baris tabel Varian penutupan, ulangi langkah 17 sampai 22 (tiga iterasi: Done, Skip, Overlay; sesudah iterasi pertama sidebar sudah collapsed sehingga langkah pembuka tidak diulang). Ambang ukuran dihitung dengan ekspansi.
- Temuan untuk QA:
  - TC-FA-CAT-641 butir b ("sidebar tidak tertinggal terbuka") mengulang butir a; keduanya diasersi sebagai dua `Verifikasi` (letak toggle dan tooltip; panel tersembunyi).
  - TC-FA-CAT-644 butir b (preferensi collapse tersimpan tidak berubah) tidak menyebut cara mengamati; spec mengamati lewat F5.
- Ukuran spec 31 langkah nominal (dengan ekspansi tiga iterasi sekitar 45), melewati sekitar 35 karena Expected dipecah per klausa (S-01). Seluruh blok satu topik (walkthrough dan state sidebar), satu kelas harness, satu dataset, tanpa aksi tulis; tiap blok memulai keadaan sidebarnya sendiri lewat langkah eksplisit sehingga bagian sesudahnya tetap bermakna; spec tidak dipecah (konvensi bagian 3, batas ukuran).

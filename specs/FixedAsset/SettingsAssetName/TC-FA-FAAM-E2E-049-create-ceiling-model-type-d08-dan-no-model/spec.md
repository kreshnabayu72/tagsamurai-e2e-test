---
id: TC-FA-FAAM-E2E-049-create-ceiling-model-type-d08-dan-no-model
title: "Create: Ceiling Model/Type (D-08), No Model Dihitung, dan Edit di Ceiling"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAM-161
  - TC-FA-FAAM-162
  - TC-FA-FAAM-164
coverage:
  web: automated
---

# Create: Ceiling Model/Type (D-08), No Model Dihitung, dan Edit di Ceiling

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client dengan katalog Model/Type satu di bawah ceiling (Pre-setup #19d). Email akun tidak tertulis di Pre-setup TC (disediakan tim FE; lihat Temuan untuk QA), `Spectra.env.FA_CEIL19D_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control client utama, `Spectra.env.FA_TC_PASSWORD`).
- Environment variable: `FA_CEIL19D_PASSWORD`, `FA_CEIL19E_PASSWORD`, `FA_CEIL19J_PASSWORD`, `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Akun aktor berikutnya (ganti akun eksplisit): Total Control client dengan katalog Model/Type tepat di ceiling dan `Plain Unit` (Pre-setup #19e, `Spectra.env.FA_CEIL19E_PASSWORD`) dan client terpisah dengan katalog Model/Type tepat di ceiling dan `Plain Unit` (Pre-setup #19j, `Spectra.env.FA_CEIL19J_PASSWORD`). Email akun client khusus tidak tertulis di Pre-setup TC (disediakan tim FE).
- State global: State global: Master Data Count Limit diturunkan ke minimum lewat seed API untuk client khusus TC ini dan dipulihkan di hook `after` (H7); suite berjalan serial (`parallel: false`). Catatan `[Limit]`: nilai `[Limit]` pada teks dialog adalah batas master data aktif yang disetel seed API (minimum yang diizinkan), dibaca dari kemampuan seed API tim BE/FE.
- Data Dinamis (suffix per run dan nomor spec): Asset Name `Create Min Item 161 {runId}-049`, `Create Min Item 162 {runId}-049`, dan `Create Min Item 164 {runId}-049` (tidak tersimpan); model `Over Ceiling {runId}-049` ditambahkan ke `Plain Unit` client #19j (client khusus TC ini, dipulihkan oleh seed API).
- Kemampuan teknis: pembacaan entri teratas Changelog sebagai baseline (S-12).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan Master Data Count Limit ketiga client khusus dan hapus model `Over Ceiling {runId}-049` dari `Plain Unit` lewat seed API.

## Test Steps

### TC-FA-FAAM-161: Create yang menambah model melewati ceiling Model/Type menampilkan dialog D-08 (client #19d)

1. Buka Changelog, catat entri teratas sebagai baseline, lalu tutup Modal Changelog
2. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
3. Isi field wajib: Asset Name `Create Min Item 161 {runId}-049`, Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, UoM `Unit`
4. Pilih Brand `Dell` dan tambahkan model `Ceil A` dan `Ceil B`
5. Klik `[Submit]`
6. Verifikasi dialog `Model/Type Limit Reached` dengan teks `You've reached the platform limit of [Limit] models. Contact support if you need a higher limit.` dan tombol `[OK]` tampil
7. Verifikasi Record tidak dibuat dan modal tetap terbuka dengan input dipertahankan
8. Pulihkan form: klik `[Clear Field]`, lalu klik `[✕]` (form bersih tertutup tanpa dialog)
9. Buka Changelog
10. Verifikasi Entri teratas Changelog sama dengan baseline (tanpa log)
11. Tutup Modal Changelog

### TC-FA-FAAM-162: Badge No Model yang disisipkan otomatis dihitung ke ceiling Model/Type (client #19e)

12. Ganti akun: keluar (Logout), lalu login sebagai Total Control client Model/Type tepat di ceiling (Pre-setup #19e; email disediakan tim FE, `Spectra.env.FA_CEIL19E_PASSWORD`), lalu buka Fixed Asset > Settings > Asset Master > Asset Name
13. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
14. Isi field wajib: Asset Name `Create Min Item 162 {runId}-049`, Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, Brand `Dell`, UoM `Unit`
15. Klik `[Submit]`
16. Verifikasi Dialog `Model/Type Limit Reached` (D-08) tampil karena badge `No Model` ikut dihitung
17. Klik `[OK]`
18. Pulihkan form: klik `[Clear Field]`, lalu klik `[✕]` (form bersih tertutup tanpa dialog)
19. Ketik Search `Create Min Item 162 {runId}-049`, tekan Enter
20. Verifikasi Empty state `No results found` tampil (record tidak dibuat)
21. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

### TC-FA-FAAM-164: Model yang ditambahkan lewat Edit tidak dievaluasi ceiling (client #19j)

22. Ganti akun: keluar (Logout), lalu login sebagai Total Control client Model/Type tepat di ceiling dengan `Plain Unit` (Pre-setup #19j; email disediakan tim FE, `Spectra.env.FA_CEIL19J_PASSWORD`), lalu buka Fixed Asset > Settings > Asset Master > Asset Name
23. Ketik Search `Plain Unit`, tekan Enter
24. Buka Edit `Plain Unit` (klik `⋯` pada baris, lalu `Edit`)
25. Tambahkan model `Over Ceiling {runId}-049` pada Brand yang sama
26. Klik `[Save]`
27. Verifikasi Edit sukses: toast `Success, asset name has been updated.` tampil
28. Verifikasi Dialog `Model/Type Limit Reached` (D-08) tidak tampil pada Edit
29. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
30. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
31. Isi field wajib: Asset Name `Create Min Item 164 {runId}-049`, Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, Brand `Dell`, UoM `Unit`
32. Klik `[Submit]`
33. Verifikasi Create berikutnya ditolak dengan dialog `Model/Type Limit Reached` (D-08)
34. Klik `[OK]`
35. Pulihkan form: klik `[Clear Field]`, lalu klik `[✕]` (form bersih tertutup tanpa dialog)

## Notes

- P-1: TC-FA-FAAM-161 butir "tanpa log" diasersi di spec asal dengan baseline Changelog langkah 1 karena precondition-nya adalah state berat (katalog Model/Type satu di bawah ceiling); S-05, S-12.
- Urutan dalam spec mengikuti client (#19d, #19e, #19j); ganti akun memakai langkah eksplisit dan sesi dikembalikan ke akun default di hook `after` (S-07).
- TC-FA-FAAM-162 dan 164 "record tidak dibuat" diasersi lewat empty state hasil Search (162) atau dialog yang menolak (164); Search adalah langkah penghubung (R-16).
- Pengisian model `Ceil A` dan `Ceil B` dipisah dari baris "Isi field wajib" karena Brand dan model adalah objek uji TC-FA-FAAM-161 (Brand `Dell` dikosongkan dari baris isi).
- Langkah pemulihan `[Clear Field]` lalu `[✕]` (langkah pemulihan setelah dialog `[OK]`) adalah langkah penghubung tanpa `Verifikasi`: form dikembalikan bersih sehingga ditutup tanpa dialog `Unsaved Changes` (S-09).
- Temuan untuk QA:
  - TC-FA-FAAM-161, 162, 164 menyebut client khusus tanpa email dan nama env akun Total Control; nama env diusulkan `FA_CEIL19D_PASSWORD`, `FA_CEIL19E_PASSWORD`, `FA_CEIL19J_PASSWORD`.
  - TC-FA-FAAM-164 menulis "Brand yang sama" tanpa menyebut Brand `Plain Unit`; spec menambahkan model pada Brand yang tertera di Popup Edit.

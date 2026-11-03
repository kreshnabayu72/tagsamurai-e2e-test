---
id: TC-FA-FAAM-E2E-056-create-ceiling-stay-hingga-ceiling
title: "Create: Ceiling dengan Stay Aktif, Data ke-N Sukses dan ke-N+1 Ditolak (D-07)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAM-163
coverage:
  web: automated
---

# Create: Ceiling dengan Stay Aktif, Data ke-N Sukses dan ke-N+1 Ditolak (D-07)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client dengan katalog Asset Name dua di bawah ceiling (Pre-setup #19f). Email akun tidak tertulis di Pre-setup TC (disediakan tim FE; lihat Temuan untuk QA), `Spectra.env.FA_CEIL19F_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control client utama, `Spectra.env.FA_TC_PASSWORD`).
- Environment variable: `FA_CEIL19F_PASSWORD`, `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Data Pre-setup #19f (disediakan lewat seed API tim BE/FE): katalog Asset Name dua di bawah ceiling Master Data Count Limit. State global: Master Data Count Limit diturunkan ke minimum lewat seed API untuk client khusus TC ini dan dipulihkan di hook `after` (H7); suite berjalan serial (`parallel: false`).
- Data Dinamis (suffix per run dan nomor spec): Asset Name `Stay Ceil 1 {runId}-056`, `Stay Ceil 2 {runId}-056`, dan `Stay Ceil 3 {runId}-056` (yang ketiga tidak tersimpan).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Stay Ceil 1` dan `Stay Ceil 2` bersuffix `{runId}-056`; pulihkan Master Data Count Limit client khusus ke nilai awal.

## Test Steps

1. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
2. Centang `Stay on this form after submitting`
3. Isi field wajib: Asset Name `Stay Ceil 1 {runId}-056`, Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, Brand `Dell`, UoM `Unit`
4. Klik `[Submit]`
5. Verifikasi Create ke-1 sukses: toast `Success, asset name has been created.` tampil
6. Verifikasi Form di-reset dan terbuka (Stay aktif)
7. Tunggu toast lama hilang otomatis
8. Isi field wajib: Asset Name `Stay Ceil 2 {runId}-056`, Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, Brand `Dell`, UoM `Unit`
9. Klik `[Submit]`
10. Verifikasi Create ke-2 sukses: toast `Success, asset name has been created.` tampil
11. Verifikasi Form di-reset dan terbuka (Stay aktif)
12. Isi field wajib: Asset Name `Stay Ceil 3 {runId}-056`, Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, Brand `Dell`, UoM `Unit`
13. Klik `[Submit]`
14. Verifikasi Create ke-3 menampilkan dialog `Asset Name Limit Reached` dengan teks `You've reached the platform limit of [Limit] asset names. Contact support if you need a higher limit.` dan tombol `[OK]` (`[Limit]` berisi batas master data aktif yang disetel)
15. Klik `[OK]`
16. Pulihkan form: klik `[Clear Field]`, lalu klik `[✕]` (form bersih tertutup tanpa dialog)
17. Ketik Search `Stay Ceil 3 {runId}-056`, tekan Enter
18. Verifikasi Empty state `No results found` tampil (record ke-3 tidak tersimpan)
19. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

## Notes

- Langkah penghubung (tanpa `Verifikasi`): menunggu toast lama hilang (R-12), `[OK]` pada dialog, pemulihan form (`[Clear Field]` lalu `[✕]`), dan Search nama sebagai pembuktian absence record ke-3 dengan empty state sebagai anchor positif (bagian 8b butir 2).
- TC-FA-FAAM-163 Expected b ("tanpa menyimpan record") diasersi lewat Search nama ke-3; TC tidak memberi cara lain mengamatinya.
- Temuan untuk QA:
  - Akun Total Control untuk client Pre-setup #19f tidak tertulis di Pre-setup TC; disediakan tim FE dengan nama env yang diusulkan `FA_CEIL19F_PASSWORD`.

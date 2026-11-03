---
id: TC-FA-FAAM-E2E-047-create-ceiling-klik-tombol-dialog-d07-dan-label-limit
title: "Create: Ceiling Master Data Count Limit pada Klik Tombol (D-07), Enterprise, dan Label Limit"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-158
  - TC-FA-FAAM-160
  - TC-FA-FAAM-677
  - TC-FA-FAAM-719
  - TC-FA-FAAM-749
coverage:
  web: automated
---

# Create: Ceiling Master Data Count Limit pada Klik Tombol (D-07), Enterprise, dan Label Limit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client dengan katalog Asset Name di ceiling (Pre-setup #19). Email akun tidak tertulis di Pre-setup TC (disediakan tim FE; lihat Temuan untuk QA), `Spectra.env.FA_CEIL19_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control client utama, `Spectra.env.FA_TC_PASSWORD`).
- Environment variable: `FA_CEIL19_PASSWORD`, `FA_CEIL19C_PASSWORD`, `FA_CEIL19H_PASSWORD`, `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Akun aktor berikutnya (ganti akun eksplisit): Total Control client Enterprise dengan katalog di ceiling (Pre-setup #19c, `Spectra.env.FA_CEIL19C_PASSWORD`) dan Total Control client dengan katalog Label tepat di batas dan katalog Asset Name di bawah batas (Pre-setup #19h, `Spectra.env.FA_CEIL19H_PASSWORD`). Email akun client khusus tidak tertulis di Pre-setup TC (disediakan tim FE).
- State global: Master Data Count Limit diturunkan ke minimum dan katalog diisi sampai tepat batas lewat seed API (Pre-setup #19, #19c, #19h), satu client per kondisi; dipulihkan di hook `after` (H7); suite berjalan serial. Catatan `[Limit]`: nilai `[Limit]` pada teks dialog adalah batas master data aktif yang disetel seed API (minimum yang diizinkan), dibaca dari kemampuan seed API tim BE/FE.
- Kemampuan teknis (disediakan tim FE): pengamatan request jaringan halaman (untuk memastikan tidak ada request pre-check terpisah).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan Master Data Count Limit ketiga client khusus ke nilai awal; tidak ada Asset Name atau Label yang dibuat spec.

## Test Steps

1. Catat jumlah total Asset Name pada tabel sebagai baseline

### TC-FA-FAAM-158: Klik [+ Asset Name] saat katalog mencapai ceiling langsung memunculkan dialog D-07

2. Klik `[+ Asset Name]`
3. Verifikasi dialog `Asset Name Limit Reached` dengan teks `You've reached the platform limit of [Limit] asset names. Contact support if you need a higher limit.` dan tombol `[OK]` tanpa CTA `[Upgrade]` tampil
4. Verifikasi `[Limit]` pada teks dialog berisi batas master data aktif yang disetel
5. Verifikasi Modal Create tidak terbuka
6. Verifikasi Tidak ada request pre-check terpisah

### TC-FA-FAAM-677: OK pada dialog D-07 menutup dialog saja

7. Klik `[OK]` pada dialog `Asset Name Limit Reached`
8. Verifikasi Dialog tertutup
9. Verifikasi Modal Create tidak terbuka
10. Verifikasi Jumlah total Asset Name pada tabel sama dengan baseline (tidak ada record dibuat)

### TC-FA-FAAM-749: Klik [+ Asset Name] saat Search aktif dengan hasil di bawah ceiling

11. Ketik Search `Tidak Ada Nama Ini`, tekan Enter
12. Verifikasi List menampilkan state kosong hasil Search (jumlah hasil 0, di bawah ceiling)
13. Klik `[+ Asset Name]`
14. Verifikasi dialog `Asset Name Limit Reached` dengan teks `You've reached the platform limit of [Limit] asset names. Contact support if you need a higher limit.` dan tombol `[OK]` tanpa CTA `[Upgrade]` tampil
15. Verifikasi Modal Create tidak terbuka
16. Klik `[OK]`, lalu klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

### TC-FA-FAAM-160: Ceiling berlaku juga pada client Enterprise dan tanpa CTA upgrade

17. Ganti akun: keluar (Logout), lalu login sebagai Total Control client Enterprise di ceiling (Pre-setup #19c; email disediakan tim FE, `Spectra.env.FA_CEIL19C_PASSWORD`), lalu buka Fixed Asset > Settings > Asset Master > Asset Name
18. Klik `[+ Asset Name]`
19. Verifikasi Dialog `Asset Name Limit Reached` (D-07) tampil
20. Verifikasi Dialog D-07 tidak memuat tombol `[Upgrade]`
21. Klik `[OK]`

### TC-FA-FAAM-719: Klik [➕] Default Label saat katalog Label sudah mencapai batas

22. Ganti akun: keluar (Logout), lalu login sebagai Total Control client dengan katalog Label di batas (Pre-setup #19h; email disediakan tim FE, `Spectra.env.FA_CEIL19H_PASSWORD`), lalu buka Fixed Asset > Settings > Asset Master > Asset Name
23. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
24. Klik tombol icon `[➕]` di sebelah caption Default Label
25. Verifikasi Dialog `Label Limit Reached` dengan teks `You've reached the platform limit of [Limit] labels. Contact support if you need a higher limit.` dan tombol `[OK]` tampil (`[Limit]` berisi batas master data aktif)
26. Verifikasi Modal Create Label tidak terbuka
27. Klik `[OK]` pada dialog
28. Verifikasi Hanya dialog yang tertutup
29. Verifikasi `Popup Create Asset Name` tetap terbuka
30. Verifikasi Modal Create Label tetap tidak terbuka
31. Klik `[✕]` (form bersih tertutup tanpa dialog)

## Notes

- Urutan dalam spec mengikuti client: client #19 untuk TC-FA-FAAM-158, 677, dan 749 (satu keadaan ceiling), lalu client Enterprise #19c, lalu client #19h; ganti akun memakai langkah eksplisit dan sesi dikembalikan ke akun default di hook `after` (S-07).
- TC-FA-FAAM-677 butir "tidak ada record dibuat" diasersi dengan jumlah total tabel terhadap baseline langkah 1.
- TC-FA-FAAM-719 Expected b dan d sama-sama menyebut Modal Create Label tidak terbuka; spec mengasersi sebelum dan sesudah `[OK]`.
- Langkah penghubung (tanpa `Verifikasi`): pencatatan baseline, `[OK]` pada dialog, penutupan Search, dan `[✕]` pada form bersih.
- Temuan untuk QA:
  - TC-FA-FAAM-158, 160, 719 menyebut client khusus (Pre-setup #19, #19c, #19h) tanpa email dan nama env akun Total Control; nama env diusulkan `FA_CEIL19_PASSWORD`, `FA_CEIL19C_PASSWORD`, `FA_CEIL19H_PASSWORD`.
  - TC-FA-FAAM-158 Expected b "tidak ada request pre-check terpisah" tidak memberi cara mengamatinya; spec memakai pengamatan request jaringan (kemampuan tim FE).

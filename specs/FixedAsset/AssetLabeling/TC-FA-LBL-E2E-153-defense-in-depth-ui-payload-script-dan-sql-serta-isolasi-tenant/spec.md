---
id: TC-FA-LBL-E2E-153-defense-in-depth-ui-payload-script-dan-sql-serta-isolasi-tenant
title: "Defense-in-Depth UI: Payload Script dan SQL serta Isolasi Tenant"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-461
  - TC-FA-LBL-462
  - TC-FA-LBL-463
coverage:
  web: automated
---

# Defense-in-Depth UI: Payload Script dan SQL serta Isolasi Tenant

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept. Langkah UI dan langkah request langsung ke server (bagian 8b butir 1: asersi request langsung hanya respons dan state data).
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson), `Fixture.assetLabeling.akun.totalControl`, `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Request langsung TC-FA-LBL-463 memakai sesi API akun yang sama. Tidak ada ganti akun di tengah spec.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak menulis ulang isinya.
- Data Pre-setup: #23 Company Beta dengan label `Beta Only` (hanya dibaca lewat fixture BE; ID label `Fixture.assetLabeling.labelBetaOnly`; request TC-FA-LBL-463 tidak boleh mengubahnya); #12 katalog Company Alpha tersedia.
- Data Dinamis (bersuffix `{runId}-153`): aset Active `Payload Asset {runId}-153` (seed fixture BE, dipakai untuk memeriksa kolom Label aset); label hasil UI `<img src=x onerror=alert(1)> 461 {runId}-153` dan `x' OR '1'='1 462 {runId}-153`.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.labelBetaOnly` | `Beta Only` (label Company Beta, Pre-setup #23) |
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): klien HTTP untuk request langsung, sesi API (login API password) per role, fixture BE untuk seeding dan membaca state katalog serta jumlah entri Changelog Labels, System Log, dan Activity Log; endpoint tidak ditulis di TC (S-13). Pembaca isi berkas ekspor CSV/XLSX untuk TC-FA-LBL-461.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus label dan aset milik spec lewat fixture BE berdasarkan ID atau nama bersuffix, tanpa berasumsi seed berhasil penuh.

## Test Steps

### TC-FA-LBL-461: Payload script pada nama label dirender sebagai teks di semua surface

1. Klik `[+ Label]`
2. Isi Label Name dengan `<img src=x onerror=alert(1)> 461 {runId}-153`
3. Klik `[Submit]`, lalu tunggu aksi selesai (modal Create Label tertutup)
4. Lampirkan label `<img src=x onerror=alert(1)> 461 {runId}-153` ke aset `Payload Asset {runId}-153` lewat fixture BE
5. Muat ulang tab Labels, ketik Search `461 {runId}-153`, tekan Enter
6. Verifikasi Labels List menampilkan nama sebagai teks literal tanpa eksekusi script
7. Buka Drawer label itu
8. Verifikasi Drawer menampilkan nama sebagai teks literal tanpa eksekusi script
9. Tutup Drawer
10. Buka Modal Changelog, lalu ketik Search `461 {runId}-153`, tekan Enter
11. Verifikasi Modal Changelog menampilkan nama sebagai teks literal tanpa eksekusi script
12. Tutup Modal Changelog
13. Buka Fixed Asset > Asset List, ketik Search `Payload Asset {runId}-153`, tekan Enter
14. Verifikasi kolom Label aset `Payload Asset {runId}-153` menampilkan nama sebagai teks literal tanpa eksekusi script
15. Buka Fixed Asset > Settings > Asset Master > tab Labels, lalu ketik Search `461 {runId}-153`, tekan Enter
16. Klik `Download` dan pilih format CSV
17. Verifikasi berkas ekspor memuat teks nama yang sama tanpa interpretasi markup
18. Ganti isi kotak search dengan `<img`, tekan Enter
19. Verifikasi Search mencocokkan keyword `<img` sebagai teks biasa (baris `<img src=x onerror=alert(1)> 461 {runId}-153` tampil)

### TC-FA-LBL-462: Payload SQL pada nama dan Search diperlakukan sebagai teks biasa

20. Klik `(←)` pada kotak Search
21. Klik `[+ Label]`
22. Isi Label Name dengan `x' OR '1'='1 462 {runId}-153`
23. Klik `[Submit]`, lalu tunggu aksi selesai (modal Create Label tertutup)
24. Ketik Search `462 {runId}-153`, tekan Enter
25. Verifikasi label tersimpan dengan nama literal `x' OR '1'='1 462 {runId}-153`
26. Ganti isi kotak search dengan `' OR 1=1 --`, tekan Enter
27. Verifikasi Search tidak mengembalikan semua baris: empty state `No results found` tampil

### TC-FA-LBL-463: Label milik client lain tidak terbaca dan tidak dapat diubah

28. Ganti isi kotak search dengan `Beta Only`, tekan Enter
29. Verifikasi `Beta Only` tidak tampil di tab Labels (empty state `No results found`)
30. Buka Modal Changelog, lalu ketik Search `Beta Only`, tekan Enter
31. Verifikasi `Beta Only` tidak tampil di Modal Changelog Company Alpha (empty state `No results found`)
32. Tutup Modal Changelog
33. Kirim request langsung ke server sebagai Total Control Company Alpha: mengambil label `Beta Only` Company Beta memakai ID-nya
34. Verifikasi respons tidak mengembalikan data `Beta Only`
35. Kirim request langsung ke server sebagai Total Control Company Alpha: mengubah label `Beta Only` Company Beta memakai ID-nya
36. Verifikasi respons tidak mengembalikan data `Beta Only`
37. Kirim request langsung ke server sebagai Total Control Company Alpha: menghapus label `Beta Only` Company Beta memakai ID-nya
38. Verifikasi respons tidak mengembalikan data `Beta Only`
39. Verifikasi nama dan warna `Beta Only` di Company Beta sama dengan sebelum permintaan (dibaca lewat fixture BE)

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 8 (Security & Defense-in-Depth). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 5, 10, 13, 15, 24, 30 adalah Search untuk menemukan baris target; bukan bagian Expected TC.
- Langkah penghubung (S-03): langkah 4, 9, 12, 20, 32 adalah navigasi, pembukaan atau penutupan modal, drawer, dialog, atau pengaturan state seeding tanpa `Verifikasi`; bukan bagian Expected TC.
- K-1: spec ini memuat TC kelas defense-in-depth (bagian 3 prinsip 13a) dengan Expected respons API; tumpang tindih dengan `tc-settings-asset-labeling-backend.md` dicatat BE pada tingkat endpoint. Berlaku untuk TC-FA-LBL-463.
- Langkah request langsung TC-FA-LBL-463 (tiga request ke label Company Beta) mengasersi hanya respons dan state data Company Beta (bagian 8b butir 1).
- Ukuran spec (39 langkah, di atas smell 35 langkah): ketiga TC satu kelas (defense-in-depth), satu akun, tanpa ganti akun, dan tiap blok memakai nama label sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah membengkak karena TC-FA-LBL-461 memeriksa enam surface (S-01).
- Temuan untuk QA:
  - TC-FA-LBL-461 Expected c "file ekspor memuat teks yang sama" tidak menyebut format berkas; spec memakai CSV lewat pembaca suite. Pemeriksaan isi berkas bukan kelas defense-in-depth murni (kelas f); TC tetap di spec ini bersama TC-FA-LBL-462 dan 463.
  - TC-FA-LBL-463 Expected a "tidak tampil di Drawer" tidak punya langkah menuju Drawer label yang tidak ada di Company Alpha; spec memeriksa tab Labels dan Modal Changelog saja.
  - TC-FA-LBL-463 tidak menyebut ID label Company Beta atau cara mendapatkannya; spec memakai ID dari fixture BE (S-13).
  - Aset berlabel untuk memeriksa kolom Label aset pada TC-FA-LBL-461 tidak disebut di precondition TC; spec men-seed aset `Payload Asset`.

---
id: TC-FA-CAID-E2E-063-resilience-timeout-60-detik-toggle-dan-edit-asset-gagal
title: "Resilience C: Save dan Toggle Melewati 60 Detik serta Edit Asset Gagal di Server"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAID-318
  - TC-FA-CAID-320
  - TC-FA-CAID-332
coverage:
  web: automated
---

# Resilience C: Save dan Toggle Melewati 60 Detik serta Edit Asset Gagal di Server

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata dan asersi state backend, bagian 6 konvensi; bukan `Mode: mock` karena sebagian asersi membaca state server).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun aktor: Total Control Company Alpha (Pre-setup No 1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Hook suite (`suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id` disetel `seen`; konfigurasi Company Alpha baseline B1 (Pre-setup No 10) dan aset A1 sampai A5 (Pre-setup No 11) dipulihkan lewat seed API sesi aktor; layar awal Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka di `beforeEach`. Suite berjalan serial (`parallel: false`).
- Nilai data dirujuk lewat `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Data Pre-setup: konfigurasi Company Alpha baseline B1 (Pre-setup No 10: Master Switch ON, Separator `/ (Slash)`, segmen Group Code, Category Code, Asset Name Code, Purchase Date, Asset Increment, tanpa Initial Company) dan aset Pre-setup No 11: A1 Active `JKT/LAP/T490/0926/1`, A2 Draft `JKT/LAP/T490/0926/2`, A3 Waiting for Approval `JKT/LAP/T490/0000/3`, A4 Disposed `JKT/LAP/T490/0926/4`, A5 Deleted (tidak tampil di UI).
- Data Pre-setup No 29 (`Company Targeted`, dipakai TC-FA-CAID-332): konfigurasi B3 (Slash dengan Group Code, Category Code, Asset Name Code, Division Code, Purchase Date, Asset Increment); aset D1 Draft `JKT/LAP/T490/0000/0000/1` (Purchase Date dan Division kosong), D2 Draft `JKT/LAP/T490/0000/0926/2` (Division kosong), D3 Draft `JKT/LAP/T490/HR/0926/3`, D4 Active `JKT/LAP/T490/HR/0926/4`, D5 Waiting for Approval. Di-seed pada Company aktor lewat sesi API di langkah penghubung (kemampuan disediakan tim FE); hook `after` memulihkan baseline B1.
- Alat uji (Pre-setup No 26): penyunting request/respons pada sesi otomasi (`Spectra.intercept()`) yang menunda respons Save dan Toggle selama 61 detik (TC-FA-CAID-318 dan 320). Penundaan 61 detik berjalan dalam waktu nyata sekitar 61 detik karena batas 60 detik adalah timeout klien yang tidak dapat digeser dengan jam server atau jam browser; jeda ini melebihi batas jeda nyata 30 detik bagian 6 konvensi; ini pilihan yang menunggu keputusan tim FE, bukan perubahan aturan. Nama endpoint konkret ditentukan tim FE di tahap script (tidak dikarang di spec).
- Pemicu kegagalan sisi server (TC-FA-CAID-332, bertanda Manual Only di TC sumber): pembaruan Asset ID otomatis akibat Edit Asset dipaksa gagal di server saat Purchase Date diisi. Kemampuan memicu kegagalan itu adalah prasyarat tahap script yang disediakan tim BE/FE dan tidak dapat dipicu dari klien.
- Kemampuan membaca jumlah entri Changelog Custom Asset ID sebelum aksi sebagai baseline N disediakan tim FE/BE (bagian 8b butir 10); jumlah entri tidak diasersi sebagai angka absolut (S-12). Surface log yang diperiksa adalah Modal Changelog: Custom Asset ID, karena TC menyebut "entri log" tanpa menyebut surface.
- Konfirmasi bawaan browser `beforeunload` ditangani otomatis oleh harness (konfirmasi tanpa langkah bersyarat) pada muat ulang tab Custom Asset ID dengan form yang masih berisi Separator belum tersimpan. Jeda 5 detik untuk mengamati toast persisten adalah pilihan spec, bukan nilai TC.
- Berkas unggah `invoice.pdf` untuk Edit Asset pada TC-FA-CAID-332 (belum ada di `fixtures/`; prasyarat tahap script yang disediakan tim FE/BE).
- Data Dinamis: tidak ada. State global: konfigurasi Company Alpha menjadi Separator `- (Dash)` dan Master Switch OFF pada TC-FA-CAID-318 dan 320 (Retroactive Mass Update), serta B3 pada TC-FA-CAID-332; dipulihkan ke baseline B1 lewat seed API sesi aktor di antara TC dan di hook `after`. Entri log yang bertambah tidak dihapus. Hook `after` juga melepas semua intercept dan pemicu kegagalan server.

## Test Steps

### TC-FA-CAID-318: Save melewati batas 60 detik

1. Catat jumlah entri Changelog Custom Asset ID sebagai baseline N
2. Pilih Separator `- (Dash)`
3. Tunda respons Save selama 61 detik, lalu klik `[Save]`
4. Verifikasi Toast `Connection problem. Please try again.` tampil tanpa tombol aksi
5. Verifikasi form tetap terbuka dengan Separator `- (Dash)`
6. Verifikasi tombol `[Save]` aktif kembali
7. Lepas penundaan respons Save
8. Klik `[Save]` lagi sebagai retry manual
9. Verifikasi Toast netral `No changes to save.` tampil
10. Muat ulang tab Custom Asset ID
11. Verifikasi form menampilkan Separator `- (Dash)` (server sudah commit pada request pertama)
12. Klik tombol `[Changelog]` pada header kartu
13. Verifikasi Modal Changelog bertambah tepat satu entri Edit Separator dibanding baseline N (tanpa mass update baru dan tanpa entri log ganda dari retry)
14. Klik `[✕]` pada header Modal Changelog
15. Buka Fixed Asset > Assets > All Assets
16. Verifikasi Asset ID A1 sampai A3 berformat Dash (`JKT-LAP-T490-0926-1`, `JKT-LAP-T490-0926-2`, `JKT-LAP-T490-0000-3`)
17. Pulihkan konfigurasi Company Alpha dan aset A1 sampai A5 ke baseline B1 lewat seed API sesi aktor, lalu muat ulang tab Custom Asset ID

### TC-FA-CAID-320: Toggle melewati batas 60 detik

18. Catat jumlah entri Changelog Custom Asset ID sebagai baseline N
19. Geser Master Switch ke OFF
20. Tunda respons Toggle selama 61 detik, lalu klik `[Disable]`
21. Verifikasi Toast `Connection problem. Please try again.` tampil tanpa tombol aksi
22. Verifikasi Master Switch kembali ke posisi ON saat toast tampil
23. Lepas penundaan respons Toggle
24. Geser Master Switch ke OFF lagi
25. Klik `[Disable]` sebagai retry
26. Verifikasi Toast netral `No changes to save.` tampil
27. Muat ulang tab Custom Asset ID
28. Verifikasi Master Switch OFF (server sudah commit pada request pertama)
29. Klik tombol `[Changelog]` pada header kartu
30. Verifikasi Modal Changelog bertambah tepat satu entri Edit Status dibanding baseline N (tanpa mass update baru dan tanpa entri log Status ganda dari retry)
31. Klik `[✕]` pada header Modal Changelog
32. Buka Fixed Asset > Assets > All Assets
33. Verifikasi Asset ID A1, A2, dan A3 berupa nomor polos `1`, `2`, dan `3`
34. Terapkan konfigurasi B3 dan aset D1 sampai D5 (Pre-setup No 29) lewat seed API sesi aktor

### TC-FA-CAID-332: Edit Asset gagal di server

35. Aktifkan pemicu kegagalan sisi server untuk pembaruan Asset ID akibat Edit Asset
36. Buka Fixed Asset > Assets > Registration
37. Klik `[Complete Detail]` pada aset D1
38. Isi Purchase Date `15/09/26`, Purchase Price `15000000`, dan unggah faktur `invoice.pdf`
39. Klik `[Save Details]`
40. Verifikasi Toast error `Error, failed to update asset.` tampil
41. Tunggu 5 detik tanpa menutup toast
42. Verifikasi toast error masih tampil (bertahan sampai di-dismiss)
43. Tutup toast error (dismiss)
44. Matikan pemicu kegagalan sisi server
45. Buka Fixed Asset > Assets > All Assets > Detail D1
46. Verifikasi Purchase Date D1 tetap kosong
47. Verifikasi Asset ID D1 tetap `JKT/LAP/T490/0000/0000/1`
48. Verifikasi tidak ada entri riwayat maupun banner pada Detail D1

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. 48 langkah, di atas 35 langkah. Alasan: seluruh blok satu kelas harness (fault injection, bagian 3 prinsip 13b), tiap blok berdiri sendiri dengan state awal dipulihkan lewat seed (langkah 17 dan 34), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah panjang berasal dari blok TC-FA-CAID-318 dan 320 yang masing-masing mengasersi retry, state setelah muat ulang, jumlah entri Changelog, dan Asset ID di All Assets.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC: TC-FA-CAID-318, 320, lalu 332. TC-FA-CAID-332 membutuhkan konfigurasi B3 pada Company Targeted (Pre-setup No 29) sehingga ditaruh paling akhir.
- Langkah penghubung (tanpa `Verifikasi`): pelepasan penundaan respons, langkah 17 (memulihkan baseline B1 sebelum TC-FA-CAID-320), langkah 34 (menerapkan B3 sebelum TC-FA-CAID-332), pengaktifan dan pematian pemicu kegagalan server, serta "Tunggu 5 detik tanpa menutup toast" dan "Tutup toast error" pada TC-FA-CAID-332.
- Muat ulang pada langkah 10 dan 27 dilakukan saat form masih berisi Separator `- (Dash)` belum tersimpan menurut UI pada langkah 10; konfirmasi `beforeunload` ditangani otomatis oleh harness (Prerequisites), tanpa langkah bersyarat (S-08).
- Pembagian TC lintas spec: TC-FA-CAID-12, 159, 230, 317, dan 321 ada di spec 061; TC-FA-CAID-316, 319, 340, 155, dan 226 ada di spec 062.
- Temuan untuk QA:
  - TC-FA-CAID-318 b dan TC-FA-CAID-320 b menyebut "tanpa mass update baru dan tanpa entri log ganda" tanpa menyebut cara mengamati mass update baru; spec mengamati lewat jumlah entri Modal Changelog yang bertambah tepat satu dibanding baseline N. Nilai entri Edit Separator (TC-FA-CAID-318) dan Edit Status (TC-FA-CAID-320) hanya diasersi sebagai jumlah.
  - TC-FA-CAID-318 dan 320 mensyaratkan jeda nyata sekitar 61 detik (timeout klien 60 detik) yang melewati jendela 30 detik bagian 6 konvensi dan tidak dapat dipersingkat dengan jam; perlu keputusan tim FE.
  - TC-FA-CAID-332 bertanda Manual Only; kolom akun menyebut Total Control (Pre-setup No 1) sedangkan data Pre-setup No 29 dinamai Company Targeted. Spec menerapkan data pada Company aktor; bila Company terpisah, diperlukan langkah ganti akun dan env var baru.
  - TC-FA-CAID-332 tidak menyebut apakah meninggalkan form Complete Detail yang gagal disimpan memunculkan dialog `Unsaved Changes`; spec tidak menulis dialog itu.

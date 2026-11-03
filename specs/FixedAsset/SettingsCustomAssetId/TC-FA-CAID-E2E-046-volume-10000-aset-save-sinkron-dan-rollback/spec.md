---
id: TC-FA-CAID-E2E-046-volume-10000-aset-save-sinkron-dan-rollback
title: "Volume 10.000 Aset: Save Sinkron Atomik dan Kegagalan Server Membatalkan Transaksi"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAID-322
  - TC-FA-CAID-323
coverage:
  web: automated
---

# Volume 10.000 Aset: Save Sinkron Atomik dan Kegagalan Server Membatalkan Transaksi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `Company Big` (Pre-setup No 22). Email akun disediakan tim FE/BE (Pre-setup No 22); password `Spectra.env.FA_BIG_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (No 22): `Company Big` dengan 10.050 aset Active (Increment 1 sampai 10050; Group `Jakarta Office` Code `JKT`, Category `IT Equipment > Laptop` Code `LAP`, Asset Name `ThinkPad T490` Code `T490`, Purchase Date 15/09/26) dan konfigurasi B1.
- Tabel "Aset yang diperiksa" (TC-FA-CAID-322, setelah Separator Dash):

  | Increment | Asset ID Dash |
  |---|---|
  | 1 | `JKT-LAP-T490-0926-1` |
  | 5025 | `JKT-LAP-T490-0926-5025` |
  | 10050 | `JKT-LAP-T490-0926-10050` |

- Kemampuan teknis: sesi API aktor dan seed API untuk `Company Big` (suite.md; seed 10.050 aset dan pengembaliannya disediakan tim FE/BE); kemampuan menghitung jumlah aset per format Asset ID (Slash atau Dash) lewat fixture BE (disediakan tim BE/FE); pemicu kegagalan server di tengah proses mass update setelah sebagian aset diproses disediakan tim BE/FE sebagai prasyarat tahap script (TC-FA-CAID-323 berlabel Manual Only karena kondisi sisi server tidak dapat dipicu dari klien); konfirmasi otomatis dialog `beforeunload` browser oleh harness untuk langkah muat ulang pada form dirty (prasyarat tahap script yang disediakan tim FE/BE); kemampuan membaca jumlah entri Object `Custom Asset ID` di Modal Changelog: Custom Asset ID, System Log (Detail User), dan Activity Log (tab User Action) sebelum aksi (disediakan tim FE/BE; audit trail permanen sehingga jumlah entri diasersi sebagai selisih terhadap baseline, S-12).
- Flag Guided Tooltip: disetel `seen` oleh hook suite untuk akun UI spec ini (suite.md); spec ini tidak menguji flag itu.
- State global: Separator `Company Big` menjadi `- (Dash)` pada TC-FA-CAID-322 dan seluruh Asset ID berubah. Hook `after` memulihkan `Company Big` ke seed awal lewat seed API dan mematikan pemicu kegagalan server. Entri log yang bertambah tidak dihapus. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-322: Save dengan lebih dari 10.000 aset diproses penuh secara sinkron dan atomik

1. Pilih Separator `- (Dash)`
2. Klik `[Save]` dan tunggu respons
3. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
4. Verifikasi Save tidak ditolak berdasarkan jumlah aset (tidak ada toast error atau alert penolakan)
5. Buka Fixed Asset > Assets > All Assets
6. Untuk setiap aset pada tabel "Aset yang diperiksa" lakukan langkah 7 sampai 9
7. Ketik Search Asset ID Dash aset itu, tekan Enter
8. Verifikasi baris aset ber-Asset ID Dash tampil dengan Asset ID sesuai tabel
9. Klik `(←)` pada kotak Search
10. Verifikasi jumlah aset ber-Asset ID Dash sama dengan 10.050
11. Verifikasi tidak ada aset yang masih berformat Slash

### TC-FA-CAID-323: Retroactive Mass Update gagal di tengah proses membatalkan seluruh transaksi

12. Atur `Company Big` ke baseline B1 (seed API), buka Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu catat baseline jumlah entri Object `Custom Asset ID` pada ketiga surface
13. Pilih Separator `- (Dash)`
14. Klik `[Save]` saat kegagalan server dipicu setelah sebagian aset diproses
15. Tunggu aksi selesai: tombol `[Save]` tidak lagi menampilkan spinner
16. Muat ulang tab Custom Asset ID
17. Verifikasi konfigurasi tersimpan tetap Separator `/ (Slash)`
18. Buka Fixed Asset > Assets > All Assets
19. Verifikasi All Assets menampilkan sedikitnya satu aset
20. Verifikasi tidak ada aset ber-Asset ID separator Dash
21. Verifikasi tidak ada aset berformat sebagian (partial)
22. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID, lalu buka Modal Changelog: Custom Asset ID
23. Verifikasi Changelog tidak memuat entri baru dibanding baseline
24. Buka Global Settings > User > Detail pengguna Sarah Johnson > tab System Log
25. Verifikasi System Log tidak memuat entri baru dibanding baseline
26. Buka Fixed Asset > Activity Log > tab User Action
27. Verifikasi Activity Log tidak memuat entri baru dibanding baseline

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah 6 sampai 9 mengulang tiga aset pada tabel "Aset yang diperiksa" (bagian 8b butir 7; ekspansi menjadi 33 langkah). Search pada langkah 7 hanya langkah penghubung untuk menemukan baris target (R-16) karena TC menyebut aset "berdasarkan Increment" tanpa cara menemukannya; `(←)` pada langkah 9 mengosongkan Search sebelum iterasi berikutnya.
- Langkah penghubung: langkah 5, 18, dan 22 (membuka halaman), langkah 12 (seed baseline dan baseline jumlah entri, S-12), langkah 15 (tunggu aksi selesai sebelum muat ulang tab dan pindah surface, bagian 8b butir 8).
- `P-1` dipakai hanya untuk asersi absence log TC-FA-CAID-323 (langkah 23, 25, dan 27): Save yang gagal dan asersi absence-nya berasal dari aksi dan seeding berat yang sama (`Company Big` 10.050 aset, Pre-setup No 22), sehingga tidak dipindah ke spec absence yang harus membangun ulang state berat itu; asersi memakai baseline jumlah entri pada langkah 12 dan anchor positif konfigurasi tersimpan sesudah muat ulang tab pada langkah 17 (S-05 dipenuhi dengan `P-1` dan baseline).
- Keberadaan TC-FA-CAID-323 (kelas b, rollback server sebagai objek uji) bersama TC-FA-CAID-322 (kelas e) di spec ini bukan pemakaian `P-2` (kegagalan di sini objek asersi, bukan pemicu) maupun `P-5` butir (b) (TC memuat state berat sendiri). Alasan tinggal di satu spec: keduanya berbagi dataset berat yang sama (`Company Big`, seed dan pengembalian disediakan tim FE/BE) dan rollback di atas 10.000 aset hanya bermakna pada volume itu. Karena tidak ada pengecualian `P-n` yang tepat, hal ini dicatat di Temuan untuk QA.
- Anchor positif asersi absence aset (bagian 8b butir 2, S-03): langkah 19 adalah `Verifikasi` generik "All Assets menampilkan sedikitnya satu aset" yang ditambahkan spec sebagai anchor bagi langkah 20 dan 21; TC-FA-CAID-323 Expected b tidak menyebut anchor itu (lihat Temuan untuk QA).
- Pembagian TC lintas spec: TC-FA-CAID-330 dan TC-FA-CAID-331 ada di spec 045.
- Temuan untuk QA:
  - TC-FA-CAID-322 langkah 3 meminta cek aset "berdasarkan Increment 1, 5025, dan 10050" tanpa menyebut cara menemukan aset di daftar; spec memakai Search pada Asset ID (asumsi kolom Asset ID dapat dicari).
  - TC-FA-CAID-322 Expected c ("jumlah aset ber-Asset ID Dash sama dengan 10.050") tidak dapat dibaca dari tabel satu halaman; spec memakai kemampuan hitung lewat fixture BE.
  - TC-FA-CAID-323 berlabel Manual Only (kondisi sisi server tidak dapat dipicu dari klien); spec tetap ditulis dengan pemicu yang disediakan tim BE/FE.
  - TC-FA-CAID-323 tidak menyebut toast atau alert saat kegagalan server; spec tidak mengasersinya.
  - TC-FA-CAID-323 Expected b (tidak ada aset ber-Asset ID separator Dash atau berformat sebagian) tidak menyebut anchor positif pada All Assets; langkah 19 spec adalah tambahan generik (S-03), bukan Expected TC.
  - TC-FA-CAID-323 langkah 3 memuat ulang tab saat form berisi perubahan belum tersimpan sehingga dialog `beforeunload` muncul; TC tidak menyebutnya dan spec menanganinya sebagai kemampuan harness.
  - Penggabungan TC-FA-CAID-322 (volume, kelas e) dan TC-FA-CAID-323 (kegagalan server sebagai objek uji, kelas b, dengan state berat) dalam satu spec tidak tercakup `P-1` sampai `P-7` secara penuh (`P-1` hanya mencakup asersi absence log); perlu keputusan konvensi atau pemisahan spec pada putaran berikutnya.
  - Post Condition TC-FA-CAID-322 dan TC-FA-CAID-323 tidak diasersi karena TC tidak memberi langkah observasinya.

# Usulan Naik ke "Di Dalam Filter": Admin Console > Tag Stock

Modul: Admin Console > Tag Stock (Stock List, Add Stock RFID dan GPS, Audit TAG, Delete by Scan, Detail SKU, Modal Event Log, Download)
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `AdminConsole/TagStock`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper atau fitur belum dibangun, spek tetap diusulkan tapi ditandai di kolom Gap.

Semua spek di modul ini berstatus "Belum ada skrip". Penilaian sepenuhnya dari dampak bisnis.

Halaman Approval belum di-slicing, jadi spek yang menguji halaman Approval dikecualikan dan tidak diusulkan (lihat bagian Dikecualikan).

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Gap |
|---|---|---|---|---|---|
| E2E-059 | Add Stock RFID: Normalisasi Identifier, Identifier Unit Rejected Terdaftar sebagai Unit Baru, dan Submit Ulang Batch yang Sama | High | Unit yang ditolak bisa terdaftar lagi sebagai unit baru, dan batch yang sama bisa masuk dua kali | Belum ada skrip | tidak |
| E2E-060 | Add Stock RFID: Bypass E2a oleh Total Control, Tidak Menampilkan Waiting, dan Unit Bypass Tidak Masuk Quantity | High | Bypass approval oleh Total Control harus tercatat dan tidak menambah kuantitas yang salah | Belum ada skrip | tidak |
| E2E-078 | Konkurensi Add Stock: Dua Sesi Submit Identifier Sama (RFID dan GPS) dan Hasil Commit Berbeda dari Badge | High | Identifier yang sama bisa masuk dua kali lewat dua sesi | Belum ada skrip | tidak |
| E2E-085 | Add Stock GPS: Validasi IMEI 15 Digit, Duplicate in File/List, Hapus Baris Preview | High | IMEI ganda bisa masuk ke stok | Belum ada skrip | tidak |
| E2E-090 | Add Stock GPS: Klik Ganda Submit, Bypass E2a oleh Total Control, dan IMEI Hanya Dipegang Unit Rejected | High | Klik ganda dan bypass yang salah bisa menambah stok dua kali | Belum ada skrip | tidak |
| E2E-131 | Audit RFID Konkurensi: Unit Berubah Status oleh Sesi Lain Di-Skip dan Nol Perubahan dengan Unit Di-Skip | High | Audit bisa menandai unit yang sudah berubah status | Belum ada skrip | tidak |
| E2E-144 | Delete by Scan: Reader Terputus, Meninggalkan Halaman, Log Sesi, dan Distributor Hanya Menghapus Stok Sendiri | High | Delete by scan bisa menghapus stok yang bukan milik distributor, atau berhenti di tengah | Belum ada skrip | tidak |
| E2E-146 | Konkurensi Audit dan Delete: Dua Sesi Audit pada Unit yang Sama, Delete Dua Kali, dan Delete Bersamaan dengan Audit | High | Unit bisa terhapus dua kali atau terhapus saat sedang diaudit | Belum ada skrip | tidak |
| E2E-147 | Konkurensi Delete: Unit Berubah Status oleh Sesi Lain, Bulk Delete Tidak Eligible, dan Bulk Delete Bersamaan | High | Delete massal bisa menghapus unit yang sudah tidak eligible | Belum ada skrip | tidak |
| E2E-163 | Audit RFID: Sesi Scan Aktif Ditinggalkan (Back Fisik, Semua Reader Putus, Pindah Tab, dan Reload) | High | Sesi audit yang ditinggalkan bisa menyisakan hasil yang salah | Belum ada skrip | tidak |
| E2E-164 | Konkurensi Audit dan Delete: Unit Menjadi In Use di Tengah Audit dan Delete Bersamaan dengan Approve Subject | High | Unit yang sedang In Use bisa terhapus | Belum ada skrip | tidak |
| E2E-077 | Absence Add Stock: Batch Seluruhnya Bypass Tanpa Entri Add Stock, dan Remove Tanpa Request atau Log | Medium | Jejak audit: bypass dan remove harus tercatat | Belum ada skrip | tidak |
| E2E-092 | Add Stock GPS Volume: Kegagalan Job Background, Ambang 5.000 Lintas Upload, Remove Menurunkan Total ke 5.000 | Medium | Kegagalan job background bisa membuat stok tidak sinkron | Belum ada skrip | tidak |
| E2E-151 | Absence Log: Delete by Scan Tanpa Penghapusan Tanpa Log dan Usage Event | Medium | Jejak audit: aksi tanpa perubahan tidak boleh mencatat entri palsu | Belum ada skrip | tidak |
| E2E-152 | Usage Event Handheld Reader: Satu Event per Sesi, dan Kegagalan Menulis Usage Event | Medium | Usage event yang hilang atau ganda merusak laporan pemakaian | Belum ada skrip | tidak |
| E2E-266 | Resilience Add Stock RFID: Kegagalan Menulis Entri TAG Log Membatalkan Transaksi Kejadiannya | Medium | Transaksi yang gagal menulis log tidak boleh tersimpan setengah | Belum ada skrip | tidak |

## Dikecualikan: Halaman Approval Belum Di-slicing

Spek berikut menguji halaman Approval. Halaman itu belum di-slicing, jadi tidak diusulkan sekarang. Bisa diusulkan setelah halaman Approval selesai di-slicing:
- E2E-100, E2E-103, E2E-104, E2E-121: Approvals Duplicate (scan ulang, approve dan reject bersamaan, activation collision, existing record). Dampaknya tinggi, dan perlu dinaikkan setelah halaman Approval siap.
- E2E-202, E2E-205 sampai E2E-211, E2E-247 sampai E2E-260, E2E-263, E2E-265: sort, filter, setup column, download, dan volume pada tab Approvals.

## Yang Tidak Dinaikkan

- Tampilan, sort, filter, setup column, dan pagination: E2E-002, E2E-009, E2E-010, E2E-016 sampai E2E-019, E2E-022 sampai E2E-027, E2E-168, E2E-171, E2E-172, E2E-174, E2E-175, E2E-176, E2E-177, E2E-179, E2E-183, E2E-184, E2E-187, E2E-189 sampai E2E-193, E2E-198, E2E-212, E2E-217, E2E-219, E2E-221, E2E-225, E2E-228, E2E-230 sampai E2E-236, E2E-238, E2E-241 sampai E2E-245, E2E-262, E2E-263, E2E-265.
- Download dan format berkas: E2E-021, E2E-037, E2E-180, E2E-195, E2E-223, E2E-244, E2E-258, E2E-260.
- Lintas modul dan format tanggal: E2E-111.
- Absence log dan preview: E2E-054, E2E-158. Dampak rendah.
- Row action dan hover: E2E-166.

## Catatan untuk FE/QA

- Semua spek di modul ini belum punya hasil run. Setelah dijalankan, daftar ini perlu dicek ulang.
- Sejumlah spek di Tag Stock (E2E-100 sampai E2E-121) menguji halaman Approval dan akan diusulkan setelah halaman Approval di-slicing.

# Usulan Naik ke "Di Dalam Filter": Admin Console > Client

Modul: Admin Console > Client (List, Create, Edit, Suspend/Unsuspend, Delete, Change Partner, Enrollment QR, Subscription, Auto-Archive, Derived Client, Changelog)
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `AdminConsole/Client`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper atau fitur belum dibangun, spek tetap diusulkan tapi ditandai di kolom Gap.

Semua spek di modul ini berstatus "Belum ada skrip", jadi kolom status tidak membedakan. Penilaian sepenuhnya dari dampak bisnis.

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Gap |
|---|---|---|---|---|---|
| E2E-014 | Pindah Group Distributor Otomatis Memindahkan Group Client Distributor-langsung | High | Perpindahan group mengubah cakupan akses client | Belum ada skrip | tidak |
| E2E-046 | Create Client oleh Active-Full: Client Code Kapital, Nama Dihapus Dipakai Ulang, Trim, dan Double-Submit | High | Client ganda bisa terbuat lewat double-submit atau kode/nama bekas | Belum ada skrip | tidak |
| E2E-054 | Create Client: Client Code dan Email Default User Milik Client yang Sudah Dihapus Dipakai Ulang | High | Data client lama bisa tertimpa atau bocor ke client baru dengan kode/email sama | Belum ada skrip | tidak |
| E2E-064 | Create Client: Dua Admin Menyimpan Company Name yang Sama Hampir Bersamaan | High | Client ganda lewat konkurensi dua admin | Belum ada skrip | tidak |
| E2E-074 | Edit Client dengan Perubahan Pelaku Kedua: Last-Write-Wins, Client Dihapus, Di-Suspend, Default User Diaktivasi | High | Edit dari sesi kedua bisa menimpa status atau menghidupkan data yang sudah di-suspend/dihapus | Belum ada skrip | tidak |
| E2E-076 | Edit Email Default User: Email Lintas Entitas, Data Client Dihapus Dipakai Ulang, Default User Tidak Dapat Dinonaktifkan | High | Email lintas entitas dan default user yang tidak bisa dinonaktifkan bisa mengunci atau membocorkan akses | Belum ada skrip | tidak |
| E2E-078 | Popup Edit Client: Saving State dan Form Tidak Ter-refresh oleh Perubahan Sesi Lain | High | Admin menyimpan dari form basi dan menimpa perubahan admin lain | Belum ada skrip | tidak |
| E2E-124 | Double-klik Konfirmasi Suspend dan Unsuspend (Tunggal dan Bulk) Hanya Memproses Satu Kali | High | Aksi ganda bisa memproses dua kali atau membalikkan status | Belum ada skrip | tidak |
| E2E-125 | Double-klik Resend Activation Email, Enable BYO, dan Delete Hanya Memproses Satu Kali | High | Email terkirim berulang dan delete ganda | Belum ada skrip | tidak |
| E2E-126 | Double-klik Tombol Konfirmasi Aksi Tulis Tidak Memproses Ganda | High | Aksi tulis ganda merusak data | Belum ada skrip | tidak |
| E2E-128 | Resend Activation Email: Jumlah Email dan Log pada Dua Klik | High | Dua klik bisa mengirim dua email dan mencatat log dobel | Belum ada skrip | tidak |
| E2E-139 | Bulk Suspend dengan Client Derived: Dialog Campuran dan Blok D-15 Tanpa Toast Sukses | High | Suspend massal bisa mengenai client yang seharusnya tidak, atau lolos tanpa peringatan | Belum ada skrip | tidak |
| E2E-140 | Bulk Selection: Select All Lintas Halaman dan Selection Limit 100 | High | Bulk action bisa melewati Selection Limit | Belum ada skrip | tidak |
| E2E-142 | Subscription Tetap Bergulir ke Expired Selama Client Suspended | High | Write lockdown: tenant Suspended tetap berubah status lewat job | Belum ada skrip | tidak |
| E2E-145 | Suspend dan Unsuspend Race Dua Tab: Aksi Idempoten | High | Changelog ganda atau Last Updated berubah tanpa perubahan nyata | Belum ada skrip | tidak |
| E2E-146 | Dua Sesi Admin: Konflik 409 pada Change Partner dan Delete Client | High | Aksi basi bisa menulis changelog yang salah | Belum ada skrip | tidak |
| E2E-147 | Suspend: Client Terpilih Sudah Disuspend atau Dihapus Pelaku Lain Sebelum Confirm | High | Suspend massal berjalan di atas data basi | Belum ada skrip | tidak |
| E2E-148 | Unsuspend: Client Terpilih Sudah Di-Unsuspend atau Dihapus Pelaku Lain Sebelum Confirm | High | Unsuspend massal berjalan di atas data basi | Belum ada skrip | tidak |
| E2E-153 | Dialog Delete: Delete Ditolak karena Izin Delete Dicabut Saat Dialog Terbuka | High | Access control: delete tetap jalan setelah izin dicabut | Belum ada skrip | tidak |
| E2E-188 | License Quota dan Quota QR Bernilai 0 pada Term Expired, Archive, Waiting for Approval, Pending, dan Trial | High | Kuota yang salah bisa membuka atau menutup kapasitas license | Belum ada skrip | tidak |
| E2E-189 | Term Trial: Kuota Terpisah dari Term Paid | High | Kuota trial bisa tercampur dengan term berbayar | Belum ada skrip | tidak |
| E2E-235 | TTL Token Enrollment QR 15 Menit: Expiry, Batas 14:59, 15:00, dan 15:01 | High | Token enrollment bisa dipakai di luar masa berlaku | Belum ada skrip | tidak |
| E2E-247 | Dua Admin: Generate Enrollment QR Bersamaan, Deactivate Station Basi, dan Revoke Tablet Basi (409) | High | Konkurensi pada perangkat terdaftar | Belum ada skrip | tidak |
| E2E-273 | Modified By Changelog Client Adalah Snapshot Nama Aktor Saat Aksi | High | Jejak audit berubah saat nama user diganti | Belum ada skrip | tidak |
| E2E-307 | Auto-Archive Dibatalkan Bila Term Baru Dibuat Saat Evaluasi Berjalan | High | Client bisa ter-archive padahal punya term aktif baru | Belum ada skrip | tidak |
| E2E-310 | Auto-Archive Setelah Cancel Term Active Terakhir | High | Term lama purge atau deleted yang salah merusak data lifecycle | Belum ada skrip | tidak |
| E2E-317 | Client Derived Saat Entitas Induk Partner Di-Suspend dan Di-Unsuspend | High | Status derived bisa salah saat induk berubah | Belum ada skrip | tidak |
| E2E-318 | Client Derived Saat Entitas Induk Partner Di-Delete | High | Client bisa terhapus atau kehilangan default user bersama | Belum ada skrip | tidak |
| E2E-319 | Client Derived Saat Entitas Induk Partner Di-Promote Menjadi Distributor | High | Managed By berpindah sehingga kepemilikan pengelolaan berubah | Belum ada skrip | tidak |
| E2E-329 | Auto-Archive Setelah Cancel Term Paid Terakhir dengan Trial Expired atau Waiting for Approval | High | Client aktif bisa terhapus dari sub-tab Archived | Belum ada skrip | tidak |
| E2E-192 | Rekonsiliasi Harian Mengoreksi Used TAG saat Push Perubahan Terlewat | Medium | Kuota TAG terpakai bisa salah dan memengaruhi batas inventaris | Belum ada skrip | tidak |
| E2E-224 | Retry Akses dari Tampilan Basi: Server Idempoten, Tidak Ada Baris Log Baru | Medium | Retry tidak boleh menulis log dobel | Belum ada skrip | tidak |

## Yang Tidak Dinaikkan

- Tampilan, tooltip, dan aksesibilitas: E2E-002, E2E-006, E2E-007, E2E-011, E2E-012, E2E-033, E2E-051, E2E-056, E2E-071, E2E-112, E2E-193, E2E-203, E2E-219, E2E-220, E2E-262, E2E-289, E2E-290, E2E-291, E2E-304, E2E-308.
- Validasi format dan batas karakter: E2E-053, E2E-082.
- Download dan pagination: E2E-301.

## Catatan untuk FE/QA

- Semua spek di modul ini belum punya hasil run. Setelah dijalankan, daftar ini perlu dicek ulang.
- E2E-014 (pindah group distributor) dinaikkan karena perpindahan group mengubah cakupan akses client. Dampak itu perlu dikonfirmasi FE/QA.

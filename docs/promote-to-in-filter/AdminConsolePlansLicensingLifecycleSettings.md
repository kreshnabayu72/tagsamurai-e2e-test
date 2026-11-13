# Usulan Naik ke "Di Dalam Filter": Admin Console > Plans Licensing > Lifecycle Settings

Modul: Admin Console > Plans Licensing > Lifecycle Settings (Trial Settings, Free Plan Settings, License Timing, Client Lifecycle, Recycle Bin, Approval Settings, System Limits, Post-Purge, Email Trigger Engine)
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `AdminConsole/PlansLicensingLifecycleSettings`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper atau fitur belum dibangun, spek tetap diusulkan tapi ditandai di kolom Gap.

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Gap |
|---|---|---|---|---|---|
| E2E-146 | Approval Settings Konsumen: Pengiriman Ulang Warning, Recalculation Berurutan, Reset, Progress Approver AND, dan Pengajuan Trial Activation | High | Aturan approval yang salah bisa meloloskan atau memblokir pengajuan trial | Gagal: 5 gap helper terbuka | ya (helper-gap: Device Allocation belum punya backend, BT-5) |
| E2E-147 | Approval Settings Konsumen: Pembatalan Manual Bersamaan dengan Job Timeout | High | Pembatalan manual dan timeout bersamaan bisa membuat status approval salah | Gagal: 1 gap helper terbuka | ya (helper-gap: Device Allocation belum punya backend, BT-5) |
| E2E-150 | Post-Purge Retention: Company dalam Archive Tidak Terpengaruh dan Hard Purge Memakai Retention Baru | High | Hard purge yang memakai retention salah bisa menghapus data yang seharusnya disimpan | Lolos tak lengkap | ya (feature-gap:be, BT-GAP-53) |
| E2E-155 | Email Trigger Engine: Email Service Gagal dan Kegagalan Cold Storage pada Transisi Grace ke Archive | High | Kegagalan cold storage bisa menghilangkan data saat transisi status | Gagal: 2 gap helper terbuka | ya (helper-gap: BT-20, BT-5) |
| E2E-156 | Email Trigger Engine: Job Terlambat, Konfigurasi Berubah, Tahapan Sebelum Pembuatan Subscription, dan Eksekusi Terlewat | High | Job yang terlambat atau terlewat bisa mengubah status subscription yang salah | Lolos tak lengkap | ya (feature-gap:be, BT-GAP-53) |
| E2E-158 | State Machine Lifecycle: Perpanjangan Membatalkan Lifecycle, Renew, Downgrade Paralel, dan Tanpa Aksi Renew pada Archive | High | Transisi state yang salah merusak siklus hidup subscription | Lolos tak lengkap | ya (sprint-gap D-098; feature-gap:be, BT-GAP-53) |
| E2E-160 | Post-Purge Archive Matching: Principal Berizin, Notifikasi Gagal, True Hard Delete, dan Principal di Luar Rantai Group | High | Hard delete yang salah sasaran menghapus data client yang masih dibutuhkan | Gagal: 4 gap helper terbuka | ya (helper-gap: BT-20, BT-5) |
| E2E-162 | Jalur Cancel Subscription: Archive Notice, Pelacak Purge Warning, dan Email Purge Confirmation | High | Pemberitahuan purge yang tidak sampai membuat data terhapus tanpa peringatan | Gagal: 3 gap helper terbuka | ya (helper-gap: BT-20) |
| E2E-164 | Countdown Reset Job Recycle Bin: Reset pada Nilai 30, Respons Save Tanpa Menunggu Job, dan Schema Client Terhapus | High | Countdown yang salah bisa menghapus data dari recycle bin terlalu cepat | Lolos tak lengkap | ya (helper-gap:be, BT-AC-LCS-4; backend diblokir) |
| E2E-181 | Save Identik No-Op Lewat Permintaan Langsung: Tab Trial Settings, Free Plan Settings, License Timing, Client Lifecycle | High | Save tanpa perubahan tidak boleh menulis changelog. Changelog harus akurat | Gagal: 4 gap helper terbuka | ya (be-bug analytics-reporting-service#48; helper-gap BT-5) |
| E2E-182 | Save Identik No-Op Lewat Permintaan Langsung: Tab Recycle Bin, Approval Settings, dan System Limits | High | Sama seperti E2E-181, untuk tab lain | Gagal: 3 gap helper terbuka | ya (be-bug analytics-reporting-service#48; helper-gap BT-5) |
| E2E-183 | Konkurensi Dua Admin: Save Bersamaan Tab Trial Settings, Free Plan Settings, dan License Timing | High | Dua save bersamaan bisa menimpa konfigurasi yang sama | Lolos tak lengkap | ya (be-bug analytics-reporting-service#48) |
| E2E-184 | Konkurensi Dua Admin: Save Bersamaan Tab Client Lifecycle, Recycle Bin, dan Approval Settings | High | Dua save bersamaan bisa menimpa konfigurasi lifecycle | Lolos tak lengkap | ya (be-bug analytics-reporting-service#48) |
| E2E-193 | Notifikasi Plan Owner dalam Aplikasi: Level Tanpa Pengguna Berizin dan Daftar Penerima Kosong | High | Plan owner tidak diberi tahu tentang trial yang akan habis | Gagal: 1 gap helper terbuka | ya (feature-gap:fe, screen belum di-slicing; helper-gap BT-20) |
| E2E-194 | Email Trigger Engine: Hard Purge Gagal dan Email Service Tetap Tidak Terjangkau Setelah Percobaan Habis | High | Hard purge yang gagal diam-diam bisa meninggalkan data yang seharusnya sudah dihapus | Gagal: 2 gap helper terbuka | ya (helper-gap: BT-20) |
| E2E-195 | Konkurensi Dua Admin: Save Bersamaan Tab System Limits dan Save Identik Akibat Save Admin Lain | High | Dua save bersamaan bisa menimpa System Limits | Lolos tak lengkap | ya (be-bug analytics-reporting-service#48) |
| E2E-196 | Countdown Reset Job Recycle Bin: Job Per-Save Gagal dengan Daily Sweep dan Item Terhapus Permanen | High | Item bisa terhapus permanen saat job gagal | Gagal: 2 gap helper terbuka | ya (helper-gap: seedFileManagerRecycleBin, BT-5) |

## Yang Tidak Dinaikkan

- E2E-008, E2E-017, E2E-038, E2E-071, E2E-116: aksesibilitas, guided tooltip, input angka, warning note, dan download changelog di atas 5.000 baris. Dampak tampilan atau volume.
- E2E-187: Save nilai minimum pada License Timing. Dampak validasi, bukan lintas data.

## Catatan untuk FE/QA

- E2E-146, 147, 155, 160, 162, 194, 196 menunggu helper dari BT-5 dan BT-20 (tidak ada route untuk membuat atau membaca term dengan state tertentu, atau memicu job). Naiknya baru berguna setelah gap ini tertutup.
- E2E-150, 156, 158 menunggu fitur di BT-GAP-53. E2E-158 juga terikat sprint D-098 (belum masuk sprint berjalan).
- E2E-181 sampai E2E-184 dan E2E-195 terkena bug backend di analytics-reporting-service#48 (changelog ganda pada save identik dan konkurensi). Spek ini perlu dinilai ulang setelah bug tertutup.
- E2E-193 menyentuh layar notifikasi yang belum di-slicing.

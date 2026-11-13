# Usulan Naik ke "Di Dalam Filter": Global Settings > Non-Login User

Modul: Global Settings > Non-Login User (List, Detail, Create, Edit, Toggle, Convert, Delete, Changelog, Tab Log)
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `GlobalSettings/NonLoginUser`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper atau fitur belum dibangun, spek tetap diusulkan tapi ditandai di kolom Gap, supaya FE tahu naiknya baru berguna setelah gap-nya tertutup.

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Gap |
|---|---|---|---|---|---|
| E2E-008 | Role Matrix: visibilitas menu User di sidebar dan direct URL tanpa capability | Medium | User tanpa hak bisa membuka halaman non-login user lewat URL langsung | Lolos tak lengkap | ui-gap (tooltip) |
| E2E-019 | Create: validasi Email sudah dipakai (Login User, Non-Login User, pending konfirmasi) | Medium | Email ganda antar jenis user merusak login dan notifikasi | Lolos | tidak |
| E2E-020 | Create: validasi Employee ID duplikat, beda huruf besar kecil, dan karakter khusus | Medium | Employee ID ganda merusak identifikasi karyawan | Lolos | tidak |
| E2E-027 | Create: Master Data Count Limit tercapai dan kuota gabungan | High | Melewati kuota berarti pelanggaran lisensi | Lolos tak lengkap | ui-defect (dialog Limit Reached) |
| E2E-032 | Storage: format GB, client tanpa kuota, batas tepat, dan 1 byte di bawah kuota | High | Kuota storage tidak ditegakkan berarti tagihan dan batas paket salah | Lolos tak lengkap | feature-gap:be (Create ditolak saat Storage penuh belum dibangun) |
| E2E-046 | Edit: validasi Email sudah dipakai | Medium | Pasangan dari E2E-019 untuk jalur Edit | Lolos | tidak |
| E2E-047 | Edit: Employee ID duplikat, karakter khusus, dan Represented By Inactive tersimpan | Medium | Pasangan dari E2E-020 untuk jalur Edit | Lolos | tidak |
| E2E-056 | Delete: user dengan Borrowed dan Assigned Asset aktif serta pemakaian ulang Email dan Employee ID | High | Menghapus user yang masih memegang aset bisa menghilangkan jejak kepemilikan aset | Lolos tak lengkap | feature-gap:be (cascade aset dan approval belum dibangun) |
| E2E-058 | Toggle Active: Switch di Detail, Temporary-expired di Detail, dan klik ganda Konfirmasi | Medium | Nonaktifkan akses yang salah atau ganda berdampak langsung ke akses user | Lolos tak lengkap | ui-gap (tooltip) |
| E2E-063 | Bulk Activate: kelompok di-skip, sebagian gagal, dan seluruh gagal | Medium | Kembaran dari E2E-064 untuk aksi Activate: bulk activate yang salah bisa memberi akses ke user yang seharusnya nonaktif atau Temporary-expired | Lolos tak lengkap | ui-gap (teks toast error belum dibuktikan di UI) |
| E2E-064 | Bulk Deactivate: kelompok di-skip, sebagian gagal, dan seluruh gagal | Medium | Bulk deactivate sebagian gagal bisa meninggalkan akses aktif tanpa diketahui admin | Gagal: nilai atau state beda (toast) | tidak |
| E2E-066 | Convert diblokir: bentrok email dengan Login User | Medium | Email yang sama di dua jenis user merusak login | Gagal: gap helper terbuka | ya (POST /v2/iam/users menolak email Login User dengan 409 sebagai helper) |
| E2E-070 | Stale: Edit, Delete, dan aksi header detail pada record dihapus atau di-convert admin lain | Medium | Edit atau hapus pada data yang sudah berubah bisa menimpa atau menghilangkan data | Lolos | tidak |
| E2E-074 | Selection Limit: live-block dan auto-cap Select All | Medium | Bulk action melewati batas Selection Limit | Gagal: gap helper terbuka | ya (System Limits tenant tidak bisa diatur lewat helper, BT-115) |
| E2E-111 | Log: entri per baris Bulk dan format kolom Changelog | Medium | Jejak audit per baris pada bulk action | Lolos tak lengkap | feature-gap:be (change-logs tanpa objectId) |
| E2E-112 | Absence log: Edit tanpa perubahan, Import, dan Delete Login User pointer | High | Jejak audit edit, import, dan delete tidak tercatat | Gagal: toast tidak muncul | ya (import job 500 untuk tenant uji, BT-GS-POS-6) |
| E2E-115 | Sinkronisasi master data: rename Position, Division, dan Custom Field | Medium | Rename master data yang tidak tersinkron membuat data user tidak konsisten | Lolos | tidak |
| E2E-116 | Sinkronisasi Import dan Convert: Detail Login User, Changelog, tab Non-Login User | Medium | Import dan convert yang tidak tersinkron merusak data user | Gagal: gap helper terbuka | ya (import job 500, BT-GS-POS-6) |
| E2E-118 | Defense-in-depth: payload skrip, perubahan tipe user, URL Detail tidak valid, isolasi entitas | Medium | Kebocoran data lintas entitas dan injeksi payload | Lolos tak lengkap | ui-defect (id entitas lain) |
| E2E-120 | State tenant: plan tier dan subscription FAMS | Medium | Gating paket yang salah membuka fitur yang tidak dibeli | Lolos tak lengkap | feature-gap:be (BT-GS-TAG-5) |
| E2E-121 | Multi-konteks: dua admin Edit, Create email sama, Employee ID sama, slot terakhir limit | Medium | Race pada email, Employee ID, dan kuota terakhir | Gagal: gap helper terbuka | ya (System Limits tidak bisa diatur, BT-115) |
| E2E-124 | Resilience aksi: kegagalan server saat Delete, Toggle, Bulk Convert, Convert | Medium | Kegagalan server di tengah aksi bisa membuat data setengah berubah | Lolos | tidak |
| E2E-125 | Role Matrix: menu `⋯` Detail tidak dirender (Create-Only, Read-Only) dan aksi tanpa kondisi Disabled | Medium | Hak Create-Only atau Read-Only bisa mengubah data | Gagal: gap helper terbuka | ya (Temporary-expired tidak bisa dibuat lewat API, TC-GS-NLU-52) |
| E2E-131 | Convert: klik ganda pada konfirmasi dan Convert dari menu Detail | High | Klik ganda pada Convert bisa membuat dua Login User dari satu Non-Login User | Lolos | feature-gap:fe (sprint-gap, layar belum di-slice) |
| E2E-137 | Sinkronisasi Login User: Deactivate, Remove Access, dan rename mempertahankan relasi Represented By | Medium | Relasi Represented By putus saat Login User diubah | Lolos tak lengkap | feature-gap:be (BT-GS-NLU-1) |

## Yang Tidak Dinaikkan

- Pola Search, Filter, Sort, Pagination, Setup Column, Download, dan Changelog di berbagai tab (002, 004, 005, 038, 039, 040, 080 sampai 098, 129, 130, 133 sampai 136, 138): pola list seragam, dampak bisnis rendah.
- Sub-tab Borrowed Assets dan Assigned Assets (101 sampai 107): layar belum di-slice (sprint-gap dan feature-gap:fe), dan sudah ditangani di modul User.
- Guided Tooltip (006, 007), Popup dirty close (028, 054), foto (017, 052), format tanggal (113), dan kosmetik lainnya.
- Validasi panjang karakter dan format (016, 044, 045, 024) dan Temporary User (021, 048, 051, 060): dampaknya kecil dibanding duplikasi atau akses.
- Referensi Position, Division, dan Custom Field dihapus sebelum Submit atau Save (022, 049, 127): pola ini belum ada keputusan khusus di modul User, jadi diperlakukan sama dengan validasi referensi lain di modul ini.
- Pembatasan 5.000 baris download (075) dan bulk select lintas halaman (061): dampaknya terbatas pada kenyamanan dan performa.
- Stale Activate dan Convert (071) dan email aktivasi Convert (072): sebagian besar tercakup oleh E2E-070.

## Catatan untuk FE

- Spek dengan Gap `ya` baru bisa lulus setelah gap-nya tertutup: helper System Limits (BT-115), helper import (BT-GS-POS-6), helper Temporary-expired, dan helper email bentrok.
- Spek dengan Gap `feature-gap` atau `ui-gap` menunggu fitur atau layar dibangun, bukan perbaikan skrip.
- Naik ke "di dalam filter" tidak berarti skrip sudah jalan. Spek tetap perlu skrip sendiri.

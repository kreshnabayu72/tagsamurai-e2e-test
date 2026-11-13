# Usulan Naik ke "Di Dalam Filter": Global Settings > Import

Modul: Global Settings > Import (Unggah Berkas, Pemetaan, Draft, Commit, Create Missing Options, Volume, Changelog Import, Multi-konteks)
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `GlobalSettings/Import`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper atau fitur belum dibangun, spek tetap diusulkan tapi ditandai di kolom Gap, supaya FE tahu naiknya baru berguna setelah gap-nya tertutup.

Semua spek di modul ini berstatus "Belum ada skrip", jadi kolom status tidak membedakan. Penilaian sepenuhnya dari dampak bisnis.

## Fitur AI Dikecualikan

Spek yang menguji saran AI (Reference Suggestion, Dismiss, Accept) tidak diusulkan, karena fiturnya belum dikerjakan dan pengetesannya memang dikecualikan. Spek-spek itu: E2E-081, E2E-118, E2E-120, E2E-121, E2E-149, dan E2E-173 (bagian AI Accept/Dismiss).

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Gap |
|---|---|---|---|---|---|
| E2E-038 | Code Division Antar-Baris dan Draft: Bentrok Append, Save Duplicate, dan Pulih Saat Baris Pembanding Dihapus atau Diubah | High | Import bisa menyimpan Division dengan Code ganda | Belum ada skrip | tidak |
| E2E-049 | Multi-Konteks Client C: Halaman Basi Setelah Draft Dihapus atau Dibuat Admin Lain, Confirm Mapping Append ke Draft yang Sudah Hilang | High | Admin bisa mengonfirmasi ke draft yang sudah dihapus atau berubah, dan data masuk tanpa sepengetahuan admin | Belum ada skrip | tidak |
| E2E-050 | Harness Worker Commit: Job Committing Dihentikan di Akhir Batch saat Entitas Suspended atau Organisasi Turun ke Plan Free | High | Commit bisa tetap menulis data saat tenant Suspended atau turun plan | Belum ada skrip | tidak |
| E2E-127 | Create Missing Divisions dan Positions saat admin lain mengubah data lebih dulu: duplicate ditolak, baris pulih, no-op dari halaman basi | High | Division atau Position ganda bisa terbuat saat dua admin bekerja bersamaan | Belum ada skrip | tidak |
| E2E-130 | Create Missing Options saat admin lain mengubah data: nama sudah ada, Custom Field dinonaktifkan atau dihapus, baris dihapus, dan Discard | High | Opsi ganda atau opsi pada Custom Field yang sudah dihapus bisa tersimpan | Belum ada skrip | tidak |
| E2E-151 | Multi-konteks Client Limit: balapan dua sesi memperebutkan slot terakhir Master Data Count Limit (Division) | High | Dua sesi import bisa melewati kuota Master Data Count Limit | Belum ada skrip | tidak |
| E2E-174 | Resilience: koneksi terputus saat Confirm Mapping, tab ditutup saat modal terbuka, gagal unduh Changelog, gagal memuat Changelog (Try Again) | High | Commit yang terputus di tengah bisa meninggalkan data setengah masuk | Belum ada skrip | tidak |
| E2E-175 | Multi-konteks: aksi mutasi pada draft yang baru dihapus admin lain (Draft Tidak Ditemukan), tujuh tab, dan Delete All Rows kategori yang sudah dihapus | High | Aksi pada draft basi bisa menimpa atau menghapus data yang sudah berubah | Belum ada skrip | tidak |
| E2E-185 | State tenant: tulis-balik evaluasi ditekan saat Suspended dan Expired, draft tersimpan saat turun ke plan Free dan naik kembali, produk Access dicabut dari organisasi | High | Tulis-balik saat Suspended atau Expired melanggar write lockdown | Belum ada skrip | tidak |
| E2E-207 | Custom Field Required yang dinonaktifkan atau dihapus tidak dievaluasi; aktif kembali berlaku retroaktif | High | Data import bisa lolos tanpa field wajib yang aktif, atau gagal secara retroaktif | Belum ada skrip | tidak |
| E2E-076 | Pelepasan Kunci saat Tab Ditutup Gagal sehingga TTL Berlaku, dan Save Ditolak setelah Capability Dicabut lalu Kunci Lepas setelah TTL | Medium | Akses yang sudah dicabut bisa tetap menulis data selama TTL kunci | Belum ada skrip | tidak |
| E2E-169 | Absence: Create Missing Options yang tidak menambah opsi apa pun tidak menulis entri log | Medium | Jejak audit: aksi yang tidak mengubah apa pun tidak boleh mencatat entri palsu | Belum ada skrip | tidak |
| E2E-203 | Entri ringkasan Changelog Import immutable, dan commit 0 baris terkomit tetap menulis satu entri | Medium | Jejak audit import harus tetap utuh dan tidak bisa diubah | Belum ada skrip | tidak |

## Yang Tidak Dinaikkan

- E2E-023, E2E-033 (penyaringan delimiter dan normalisasi nilai sel): validasi format dan parsing, dampak sedang. Pola validasi sudah dinilai di modul lain.
- E2E-035, E2E-036, E2E-041, E2E-042 (validasi panjang karakter dan emoji): pola validasi yang seragam.
- E2E-051, E2E-052, E2E-053, E2E-054 (umur draft 24 jam dan TTL berkas): aturan waktu, dampak sedang.
- E2E-056, E2E-057, E2E-079 (batas 10.000 baris dan 1 MB): batas teknis, bukan kuota bisnis.
- E2E-086 (presedensi status error): urutan pesan validasi.
- E2E-111, E2E-190, E2E-197 (Select All, Delete All Rows, kartu, Modal Changelog): tampilan dan pola list.
- E2E-144 (download template dan unggah ulang): alur normal, dampak sedang.
- E2E-161 (notifikasi progres commit): notifikasi.
- E2E-178 (volume 150 baris pada Selection Limit 100): pagination dan filter kartu.
- E2E-077 (kontrol worker commit): tooltip dan konflik proses yang sudah tercakup oleh E2E-050.
- E2E-193, E2E-198, E2E-200 (format tanggal dan urutan Changelog): tampilan.
- E2E-005, E2E-062 (Guided Tooltip dan Android): tampilan.
- E2E-106, E2E-139, E2E-209, E2E-210, E2E-218 (kolom Phone, footer, banner, dan Android): tampilan.

## Catatan untuk FE/QA

- Semua spek di modul ini belum punya skrip. Setelah skrip dibuat, daftar ini perlu dicek ulang terhadap hasil run.
- Spek yang dinaikkan karena alasan concurrency (038, 049, 127, 130, 151, 175) menguji dua sesi admin. Mekanisme sesi kedua belum didefinisikan di beberapa TC.

## Catatan untuk Anda: Konsistensi Spek Belum Ada Skrip

Di modul-modul sebelumnya (misalnya AllTags, Mobile, dan Guided Tooltip), saya menggugurkan spek High yang berstatus "Belum ada skrip" atau belum dijalankan dengan alasan belum ada skrip atau surface belum dibangun. Itu tidak konsisten dengan kriteria Anda, yaitu dampak bisnis tanpa melihat status run. Contohnya AllTags E2E-015 (High, mobile) dan E2E-011 (Medium). Kalau Anda setuju, saya bisa menilai ulang spek-spek itu dengan kriteria yang sama dan memperbarui dokumennya.

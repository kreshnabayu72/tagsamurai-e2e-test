# Usulan Naik ke "Di Dalam Filter": Global Settings > Hardware Handheld Reader

Modul: Global Settings > Hardware Handheld Reader (Daftar Reader, Activate, Mark as Damaged, Filter, Changelog, Event Log, Multi-konteks)
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `GlobalSettings/HardwareHandheldReader`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper, fitur, atau hardware yang belum tersedia, spek tetap diusulkan tapi ditandai di kolom Gap, supaya FE tahu naiknya baru berguna setelah gap-nya tertutup.

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Gap |
|---|---|---|---|---|---|
| E2E-025 | Activate Reader: Saving State Tombol Submit dan Klik Ganda Cepat pada Submit | High | Klik ganda bisa mengaktifkan reader dua kali, dan itu memakai slot kuota | Lolos tak lengkap | hardware-gap (langkah tertentu membutuhkan TAG hardware, D-097) |
| E2E-047 | Selection Limit Bulk Reader Client SL: Checkbox ke-(Limit+1) Disabled dan Select All Dipotong ke Limit | High | Bulk action bisa melewati Selection Limit | Belum dijalankan | tidak |
| E2E-048 | Multi-Konteks: Bulk Mark as Damaged saat Sebagian atau Seluruh Reader Terpilih Sudah Diubah Admin Lain Sebelum Konfirmasi | High | Mark as Damaged pada reader yang sudah diubah admin lain bisa menimpa status atau menandai reader yang salah | Lolos tak lengkap | feature-gap:be (route write Handheld Reader belum dibangun) |
| E2E-073 | Konkurensi Dua Admin: Edit Alias Name, Edit Reader Power, Mark as Damaged, dan Edit pada Reader yang Dihapus | High | Edit bersamaan bisa menimpa data reader, dan edit pada reader yang sudah dihapus bisa menghasilkan data basi | Lolos tak lengkap | feature-gap:be (Admin B belum punya support action untuk write Handheld Reader) |
| E2E-075 | Konkurensi Aktivasi: Kuota Habis Sebelum Submit, Dua Admin pada Slot Kuota Terakhir, dan Serial Number yang Sama | High | Dua admin bisa melewati kuota aktivasi, dan serial yang sama bisa terdaftar dua kali | Lolos tak lengkap | hardware-gap (langkah tertentu membutuhkan TAG hardware, D-097) |

## Yang Tidak Dinaikkan

- E2E-052 (filter rentang Reader Power, Last Scanned, dan Activated At): logika filter tampilan, dampak data tidak berubah, dan spek ini lolos.
- E2E-007 (Guided Tooltip): tampilan, dampak rendah. Belum ada skrip.
- E2E-056 (Setup Column tabel sekunder): pola Setup Column yang seragam. Belum ada skrip.
- E2E-059 (download lebih dari 5.000 baris): volume, prioritas Low. Belum ada skrip.
- E2E-078 (opsi dropdown Device Name dan loading): tampilan filter, prioritas Low. Belum ada skrip.

## Catatan untuk FE/QA

- E2E-025 dan E2E-075 memakai langkah yang membutuhkan TAG hardware (D-097). Di stack uji tanpa hardware, langkah itu dilewati, jadi bukti lolosnya belum utuh.
- E2E-048 dan E2E-073 bergantung pada route write Handheld Reader untuk Admin B. Route itu belum ada di support action. Kalau belum tersedia, spek ini tidak bisa lulus.
- E2E-047 belum dijalankan. Penilaian dampaknya sama dengan spek Selection Limit di modul lain, tapi hasil run-nya belum ada.
- Daftar ini hanya mencakup 10 spek yang diajukan untuk Hardware Handheld Reader.

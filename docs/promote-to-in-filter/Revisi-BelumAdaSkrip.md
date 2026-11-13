# Revisi: Spek Belum Ada Skrip yang Dinilai Ulang

Tanggal: 2026-11-13

## Latar Belakang

Di dokumen modul sebelumnya, sebagian spek High atau Medium saya gugurkan karena statusnya "Belum ada skrip" atau "Belum dijalankan". Penilaian itu tidak sesuai kriteria, yaitu dampak bisnis tanpa melihat status run. Dokumen ini menilai ulang spek-spek tersebut dengan kriteria yang sama.

Fitur AI dan surface mobile belum dibangun, jadi spek-spek yang menguji keduanya dikecualikan dan tidak diusulkan.

## Keputusan

### AllTags (`AllTags.md`)

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status | Gap |
|---|---|---|---|---|---|
| E2E-011 | Plan Free: Audit atas Tipe Terkunci Tanpa Baris dan Delete by Scan atas Tag Terkunci Ditolak | Medium | Tag yang terkunci oleh plan bisa terhapus lewat scan | Belum ada skrip | tidak |
| E2E-062 | Un-Retire Ditolak oleh Supply Asset saat Kuota Tipe Penuh atau Terpakai Melebihi Kuota | Medium | Un-retire yang melewati kuota tipe TAG menambah inventaris di luar batas | Belum ada skrip | tidak (selector dan copy penolakan belum didefinisikan di TC) |

## Dikecualikan: Surface Mobile Belum Dibangun

Spek-spek berikut menguji surface mobile dan tidak diusulkan:
- AllTags E2E-015 (High): aksi massal dan visibilitas tombol di mobile.
- Position E2E-027 (Medium): bulk delete lewat long-press di mobile.
- Measurement E2E-075 (Medium): bulk delete unit di mobile.
- Brand E2E-074 (Medium): bulk delete brand di mobile.
- Role E2E-013 (Medium): bulk Remove hak akses lewat mobile.
- Division E2E-080, General Settings E2E-012 dan E2E-013, Role E2E-012 dan E2E-014: juga mobile, dampak rendah.

## Yang Tetap Tidak Dinaikkan

- HardwareHandheldReader E2E-007, E2E-056, E2E-059, E2E-078: tampilan atau prioritas Low.
- AllTags E2E-005, E2E-037, E2E-077, E2E-079, E2E-080, E2E-085, E2E-100, E2E-101: tampilan, tooltip, atau download.

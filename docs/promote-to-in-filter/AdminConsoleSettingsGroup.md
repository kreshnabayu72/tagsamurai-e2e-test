# Usulan Naik ke "Di Dalam Filter": Admin Console > Settings > Group

Modul: Admin Console > Settings > Group (Tabel Utama, Create, Edit, Delete, Bulk Delete, Changelog, Absence Log, Konkurensi, Mobile)
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `AdminConsole/SettingsGroup`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper atau fitur belum dibangun, spek tetap diusulkan tapi ditandai di kolom Gap.

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Gap |
|---|---|---|---|---|---|
| E2E-036 | Edit Group: Huruf Besar/Kecil, Nama Sama pada Parent Berbeda, Trim, dan Rename Default Group | High | Nama ganda atau rename default group bisa merusak referensi | Lolos | tidak |
| E2E-037 | Edit Group: Unsaved Changes Bersyarat, Tanpa Pindah Parent, dan Referensi User/Entitas Tidak Putus | High | Edit yang salah bisa memutus referensi user dan entitas | Belum ada skrip | tidak |
| E2E-043 | Bulk Delete: Seleksi Lintas Halaman dan Search, Reset oleh Node, Batas Node Terpilih, dan Cancel | High | Bulk delete bisa melewati batas node terpilih | Lolos | tidak |
| E2E-047 | Bulk Delete: Selection Limit 100 pada Seleksi Manual dan Select All | High | Bulk delete bisa melewati Selection Limit | Belum ada skrip | tidak |
| E2E-074 | Modal Changelog: Setup Column, Tutup Modal, dan Snapshot Immutable | High | Jejak audit harus tetap utuh | Belum ada skrip | tidak |
| E2E-090 | Absence Log Edit Group Tanpa Perubahan di Changelog, Activity Log, dan System Log | High | Jejak audit: edit tanpa perubahan tidak boleh tercatat | Belum ada skrip | tidak |
| E2E-100 | Konkurensi Dua Admin: Create Duplikat, Edit Bersamaan, Refresh SSE, dan Fallback F5 | High | Dua admin bisa membuat group ganda atau menimpa edit | Belum ada skrip | tidak |
| E2E-101 | Konkurensi Dua Admin: Perubahan saat Delete Menunggu Konfirmasi dan Member Baru saat Bulk Delete | High | Delete massal bisa mengenai member baru yang belum dilihat admin | Lolos tak lengkap | ya (be-bug BT-GAP-34, ems#132) |
| E2E-106 | Total User dan Total Member Agregat All Groups adalah Distinct, Bukan Penjumlahan per Node | High | Angka agregat yang salah menyesatkan keputusan penagihan dan kapasitas | Belum ada skrip | tidak |
| E2E-111 | Bulk Delete: Guard Entitas Tiga Campur, Dua dari Tiga Group Lolos dan Ketiganya Lolos karena Satu Di-skip | High | Guard entitas yang gagal bisa membiarkan group yang masih dipakai ikut terhapus | Belum ada skrip | tidak |

## Yang Tidak Dinaikkan

- Mobile: E2E-107 (akses changelog dan popup sebagai bottom sheet). Surface mobile belum dibangun.
- Guided tooltip dan tampilan: E2E-013, E2E-004, E2E-032.
- Filter dan search: E2E-050, E2E-051, E2E-052, E2E-054, E2E-055, E2E-063, E2E-065.
- Kolom dan sort: E2E-061, E2E-072, E2E-073, E2E-081, E2E-066 (format export dan tooltip; status Gagal karena tipe sel XLSX berbeda, perlu dicek format).
- Popup: E2E-045 (collapse bulk delete). Dampak UI.
- Lainnya: E2E-110 (fallback seleksi setelah delete ancestor, dampak seleksi tampilan).

## Catatan untuk FE/QA

- E2E-101 gagal karena bug backend BT-GAP-34 (ems#132). Perlu dinilai ulang setelah bug tertutup.
- E2E-066 gagal karena sel numerik di XLSX terbaca sebagai string, dan tooltip hierarki tidak lengkap. Ini bukan data yang salah, tapi format berkas. Dinilai tidak naik.

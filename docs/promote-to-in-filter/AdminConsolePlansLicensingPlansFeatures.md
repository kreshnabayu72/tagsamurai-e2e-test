# Usulan Naik ke "Di Dalam Filter": Admin Console > Plans Licensing > Plans & Features

Modul: Admin Console > Plans Licensing > Plans & Features (Plans List, Create/Edit Custom dan Default Plan, Archive, Delete, Global Settings, Assigned Clients, Setup Column, Changelog)
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `AdminConsole/PlansLicensingPlansFeatures`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper atau fitur belum dibangun, spek tetap diusulkan tapi ditandai di kolom Gap.

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Gap |
|---|---|---|---|---|---|
| E2E-013 | Konkurensi Dua Admin: Create Custom Plan dan Default Plan Bersamaan serta Ceiling Paid | High | Dua admin bisa membuat plan ganda atau melewati ceiling paid | Belum dijalankan | tidak |
| E2E-014 | Konkurensi Edit vs Edit Custom dan Default Plan serta Save Global Settings Bersamaan (Last-Write-Wins) | High | Edit bersamaan menimpa konfigurasi plan | Belum dijalankan | tidak |
| E2E-016 | Konkurensi Delete: Retry Delete Custom dan Default Plan serta Plan Name Diklik Setelah Plan Dihapus Sesi Lain | High | Delete ulang pada plan yang sudah dihapus bisa menulis data yang salah | Belum dijalankan | tidak |
| E2E-017 | Konkurensi: Template Di-archive Sesudah Form Create Dibuka dan Push Update ke Client yang Sudah Terbaru | High | Plan yang sudah di-archive bisa tetap didorong ke client | Belum dijalankan | tidak |
| E2E-085 | Edit Custom dan Default Plan: State Submitting dan Klik Ganda pada Save | High | Klik ganda bisa menyimpan dua kali | Belum dijalankan | tidak |
| E2E-093 | Edit Custom Plan: API call quota Custom Bernilai Sama dengan Preset | High | Plan gating: kuota yang salah membuka atau menutup kapasitas API | Belum dijalankan | tidak |
| E2E-094 | Edit Default Plan Growth: API call quota Custom Sama dengan Preset dan Format Nilai Changelog | High | Plan gating: kuota default plan yang salah | Belum dijalankan | tidak |
| E2E-101 | Guard Cannot Archive Plan: Status yang Tidak Menahan, Daftar Banyak Client, dan Dialog Backdrop | High | Plan yang masih dipakai bisa ter-archive | Belum dijalankan | tidak |
| E2E-104 | Delete Plan Archived yang Seluruh Term-nya Deleted | High | Delete plan yang masih punya term aktif merusak data | Belum dijalankan | tidak |
| E2E-111 | Archive Default Plan: Tier Tertinggi, Tier Terendah, dan Last Modified Plan yang Tergeser | High | Archive tier yang salah mengubah urutan dan ketersediaan plan | Belum dijalankan | tidak |
| E2E-112 | Delete Default Plan Archived Bekas Template: Custom Plan Turunan Tidak Berubah | High | Delete default plan tidak boleh mengubah custom plan turunan | Belum dijalankan | tidak |
| E2E-128 | Global Settings: Klik Ganda Save, State Submitting, dan Isi Entri Changelog Global Settings | High | Klik ganda bisa menulis changelog dua kali | Belum dijalankan | tidak |
| E2E-173 | Tab Assigned Clients: client yang hanya punya term terminal tidak dirender dan tidak dihitung | High | Jumlah client per plan yang salah berdampak ke penagihan | Belum dijalankan | tidak |
| E2E-177 | Tab Assigned Clients: client bertermin campuran dan term Trial | High | Penghitungan client campuran yang salah berdampak ke penagihan | Belum dijalankan | tidak |
| E2E-058 | Create Custom Plan Product SAMS dan SIEM Memakai Payload Fitur FAMS | Medium | Payload fitur yang salah membuat entitlement produk salah | Belum dijalankan | tidak |
| E2E-174 | Created By dan Assigned By sebagai nilai tersimpan saat akun pembuat atau pemberi tugas dihapus atau dinonaktifkan | Medium | Jejak audit: atribusi pembuat tidak boleh hilang saat akun dihapus | Belum dijalankan | tidak |

## Yang Tidak Dinaikkan

- E2E-046: tooltip keyboard dan wrap teks. Tampilan. Status Gagal karena menu row action, bukan gap data.
- E2E-049: batas panjang dan emoji nama plan. Validasi format.
- E2E-053: spinner dan nilai bukan kelipatan API call quota. Validasi format.
- E2E-018 sampai E2E-023, E2E-027, E2E-041, E2E-042, E2E-043, E2E-044: aksesibilitas, guided tooltip, dan tampilan list.
- E2E-004, E2E-120, E2E-138, E2E-152, E2E-153, E2E-154, E2E-158, E2E-168, E2E-187, E2E-199: loading, format tanggal, setup column, dan kolom changelog.
- E2E-118: unsaved changes Global Settings. Status Lolos.
- E2E-201: download changelog di atas 5.000 baris. Status Gagal karena nama berkas berbeda. Ini bug kecil pada nama berkas, bukan masalah data.

## Catatan untuk FE/QA

- E2E-201 gagal karena nama berkas unduhan yang berbeda dari yang diharapkan (Activity-Log-User-Action.csv, bukan Changelog-Plans-Features-Default.csv). Perlu dicek di FE.
- E2E-046 gagal karena menu row action kehilangan fokus, bukan karena data.

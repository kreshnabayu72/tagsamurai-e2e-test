# Usulan Naik ke "Di Dalam Filter": Admin Console > Settings > Device SKU

Modul: Admin Console > Settings > Device SKU (List, Register, Edit, Foto, Bulk Delete, Plan Tier, Usage, Changelog, Guided Tooltip, Mobile)
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `AdminConsole/SettingsDeviceSku`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper atau fitur belum dibangun, spek tetap diusulkan tapi ditandai di kolom Gap.

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Gap |
|---|---|---|---|---|---|
| E2E-070 | Edit SKU: Mengubah Lalu Mengembalikan Nilai Dianggap Tanpa Perubahan dan Perubahan Kapitalisasi Dicatat | High | Jejak audit: perubahan harus tercatat dengan benar, dan perubahan palsu tidak boleh tercatat | Lolos | tidak |
| E2E-172 | Resilience Foto Staging: Submit atau Save Gagal setelah Foto di Staging Tidak Membuat Foto Permanen | High | Foto yatim bisa tersimpan permanen tanpa SKU | Gagal: elemen "Photo" bukan Field yang valid | tidak |
| E2E-182 | Plan Tier: Register, Edit, dan Delete Berperilaku Identik pada Starter, Growth, Professional, dan Enterprise | Medium | Plan gating: perbedaan perilaku antar tier bisa membuka atau menutup fitur | Gagal: 1 gap helper terbuka | ya (helper-gap: hanya satu Principal yang bisa ada, Pre-setup #20 sampai #23, #38, #41) |
| E2E-189 | Bulk Delete: Hasil Aktual Menentukan Toast saat Preview Campuran Menjadi Homogen dan Homogen Menjadi Campuran | High | Toast yang salah membuat admin mengira penghapusan berhasil atau gagal | Lolos tak lengkap | ya (helper-gap:be, BT-GS-HHR-3) |

## Yang Tidak Dinaikkan

- Mobile: tidak ada di modul ini.
- Foto dan volume: E2E-065 (foto batas dua dan resize), E2E-175 (download 5.001 dan 5.000 baris, helper-gap belum ada: tidak ada helper yang membuat data sebanyak itu). Dampak volume dan format foto.
- Tampilan, aksesibilitas, dan tooltip: E2E-006, E2E-013, E2E-053, E2E-136, E2E-190.
- Register dan form: E2E-037 (trim dan emoji), E2E-045 (register berturut-turut). E2E-037 dan E2E-045 menguji validasi, dan E2E-045 terhalang dialog foto.
- Filter list: E2E-095 (helper-gap, Principal kedua tidak bisa dibuat). Dampak rendah dan terhalang helper.
- Usage dan sidebar: E2E-177 (tenant Suspended dan Expired tetap bisa membaca, feature-gap:fe dan sprint-gap). Dampak tampilan. Tulis di Suspended sudah diuji di modul lain.

## Catatan untuk FE/QA

- E2E-182 bergantung pada Principal kedua. Sistem hanya mengizinkan satu Principal, jadi perlu helper untuk membuat data plan tier.
- E2E-189 bergantung pada backend (BT-GS-HHR-3).
- E2E-172 gagal karena elemen "Photo" tidak valid sebagai Field. Perlu dicek di FE.

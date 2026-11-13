# Usulan Naik ke "Di Dalam Filter": Admin Console > Settings > User

Modul: Admin Console > Settings > User (User List, Detail User, Popup Assign Group Role, Deactivate, Activate, Resend Activation Email, Tab Responsibilities, Changelog, System Log, User Log, Download)
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `AdminConsole/SettingsUser`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper atau fitur belum dibangun, spek tetap diusulkan tapi ditandai di kolom Gap.

Modul ini mengatur akses user, jadi kriteria dampak diterapkan ketat pada deactivate, konkurensi, dan perlindungan actor sendiri.

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Gap |
|---|---|---|---|---|---|
| E2E-033 | Selection Limit: Live-block Checkbox ke-(Limit+1) dan Select All yang Melebihi Limit di-cap Otomatis | High | Bulk action bisa melewati Selection Limit | Belum ada skrip | tidak |
| E2E-164 | Pencatatan Edge Changelog User, Snapshot Entri Lama, Dua Permission Sekaligus, Save Popup Assign Group Role tanpa Perubahan, dan Save 0 Group | High | Jejak audit akses: entri lama tidak boleh berubah, dan save tanpa perubahan tidak boleh tercatat | Belum ada skrip | tidak |
| E2E-184 | Konkurensi Dua Aktor Memakai Last-Write-Wins dan Request Lama Menjadi No-Op pada Deactivate, Activate, Save Assign Group Role, dan Dialog Auto-Revert | High | Request basi bisa menimpa status user | Belum ada skrip | tidak |
| E2E-185 | Konkurensi Deactivate User Sedang Login, Dua Aktor Mengubah Status, Resend Saat Cooldown Aktor Lain, dan Switch Role Request Lama | High | User yang sedang login bisa tetap aktif setelah dinonaktifkan | Belum ada skrip | tidak |
| E2E-186 | Double-Click dan Double-Submit pada Dialog Deactivate, Bulk Deactivate, dan Bulk Activate Hanya Memproses Satu Request | High | Klik ganda pada deactivate dan activate massal | Belum ada skrip | tidak |
| E2E-187 | Double-Click dan Double-Submit pada Checkbox CRUD, Resend Activation Email, dan Save Popup Assign Group Role | High | Klik ganda bisa mengirim email dan menulis hak dua kali | Belum ada skrip | tidak |
| E2E-006 | User List: Row Action Baris Default User dan Baris Aktor Sendiri per Varian Status | Medium | Aktor bisa men-deactivate dirinya sendiri atau default user lewat row action | Belum ada skrip | tidak |

## Yang Tidak Dinaikkan

- Tampilan, tooltip, dan guided tooltip: E2E-003, E2E-010, E2E-014, E2E-067, E2E-094, E2E-095, E2E-096, E2E-100, E2E-119.
- Filter dan search tab Responsibilities, Changelog, System Log, User Log, dan Modal Changelog Group Role serta Global Role: E2E-097 sampai E2E-099, E2E-101, E2E-102, E2E-104 sampai E2E-112, E2E-114 sampai E2E-118, E2E-121 sampai E2E-125, E2E-127 sampai E2E-137, E2E-139 sampai E2E-154, E2E-195 sampai E2E-206. Dampak tampilan dan filter.
- Resilience download: E2E-181, E2E-200. Dampak notifikasi error dan download.
- Lainnya: E2E-082, E2E-083 (sort dan kombinasi list), E2E-091, E2E-092 (custom field, dampak tampilan), E2E-191 (resend tanpa batas harian, Low), E2E-069 (Low).

## Catatan untuk FE/QA

- Spek konkurensi (E2E-184, 185) menguji dua aktor. Mekanisme dua aktor di spec perlu didefinisikan di TC.
- E2E-191 (resend activation tanpa batas harian) dinilai Low. Tapi kalau ada batas harian yang belum diterapkan, ini bisa jadi risiko spam. Perlu konfirmasi PRD.

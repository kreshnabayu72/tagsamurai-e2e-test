# Usulan Naik ke "Di Dalam Filter": Admin Console > Settings > Role & Permission

Modul: Admin Console > Settings > Role & Permission (Read Only, Group Manager, Total Control, Role Detail, Assign, Remove, Bulk Remove, Guided Tooltip, Changelog, Absence Log, Mobile)
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `AdminConsole/SettingsRolePermission`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper atau fitur belum dibangun, spek tetap diusulkan tapi ditandai di kolom Gap.

Modul ini mengatur hak akses, jadi kriteria dampak diterapkan ketat pada konflik assign, remove, dan perlindungan Total Control.

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Gap |
|---|---|---|---|---|---|
| E2E-052 | Edit CRUD: Assignment Descendant, Peran Global Target GM, dan Susun Ulang Peran Manual Tanpa Auto-Revert | High | Edit CRUD bisa mengubah hak descendant atau mencabut hak tanpa sengaja | Belum ada skrip | tidak |
| E2E-057 | Bulk Remove Role Detail: Partial Success dan 0 Baris Berhasil karena Baris Berubah oleh Admin Lain | High | Bulk remove bisa mencabut hak yang salah atau melaporkan keberhasilan yang tidak terjadi | Belum ada skrip | tidak |
| E2E-111 | Double Submit: Klik Assign dan Confirm Ganda Tanpa Efek Ganda, serta Total Control Selalu Minimal Satu | High | Double submit bisa membuat assign ganda, dan Total Control bisa habis sampai tidak ada admin | Belum ada skrip | tidak |
| E2E-117 | Target Berubah sejak Render: Edit CRUD, Remove Total Control, Read Only, dan Group Manager yang Sudah Diubah Admin Lain | High | Admin bisa mencabut hak berdasarkan data yang sudah basi | Belum ada skrip | tidak |
| E2E-118 | Target Berubah sejak Render: Remove Idempoten, Approver Sudah Hilang, dan Status Target Berubah menjadi Total Control | High | Remove pada target yang sudah berubah bisa mencabut Total Control | Belum ada skrip | tidak |
| E2E-119 | Target Berubah sejak Render: Group Terpilih Dihapus Admin Lain sebelum Submit Assign Group Manager dan Assign User to Role | High | Assign ke group yang sudah dihapus bisa memberi hak ke group yang salah | Belum ada skrip | tidak |
| E2E-137 | Target Berubah sejak Render: Node Group Aktif Dihapus Admin Lain sebelum Assign Approver dan Perubahan Toggle | High | Approver bisa ditetapkan ke node yang sudah tidak aktif | Belum ada skrip | tidak |
| E2E-029 | Checkbox CRUD: Nonaktif Sementara saat In-flight dan Operasi Keyboard | Medium | Checkbox yang aktif saat in-flight bisa memicu tulis ganda | Belum ada skrip | tidak |
| E2E-063 | Resilience Tulis Approver: Bulk Remove, Assign, dan Remove Gagal 5xx | Medium | Kegagalan tulis di tengah bisa meninggalkan hak setengah berubah | Belum ada skrip | tidak |
| E2E-069 | Volume Selection Limit: Select All dan Centang Manual pada Role Detail serta Popup Assign Total Control | Medium | Selection Limit bisa terlewati saat assign Total Control | Belum ada skrip | tidak |
| E2E-109 | Modul Konsumen: Total Control Fallback Reviewer, GM Baru Tanpa Snapshot, Wallet Deposit, dan Approver TAG Stock | Medium | Fallback Total Control dan approver yang salah bisa memberi hak ke pihak yang keliru | Belum ada skrip | tidak |
| E2E-110 | Multi-Konteks: Dua Reviewer Approve Bersamaan, Permission Baru pada Sesi Paralel, Dua Admin Edit Cell Sama, dan Dua Assign Bersamaan | Medium | Konkurensi pada hak akses bisa memberi hak ganda atau menimpa | Belum ada skrip | tidak |
| E2E-116 | Defense-in-depth: Selection Limit lewat Request Langsung Ditolak (Bulk Remove dan Assign Total Control) | Medium | Selection Limit harus ditegakkan di server, bukan hanya di UI | Belum ada skrip | tidak |
| E2E-125 | Resilience Tulis: Assign dan Remove Read Only serta Assign dan Remove Group Manager Gagal 5xx | Medium | Kegagalan tulis bisa meninggalkan hak setengah berubah | Belum ada skrip | tidak |
| E2E-127 | Bulk Remove Role Detail: Baris yang Sudah Dihapus Admin Lain Dianggap Sukses | Medium | Laporan sukses yang salah menyesatkan admin | Belum ada skrip | tidak |
| E2E-129 | Assign Approver: Activation Status User Berubah Menjadi Tidak Eligible (V-09) | Medium | User yang tidak aktif bisa tetap ditetapkan sebagai approver | Belum ada skrip | tidak |
| E2E-138 | Absence Log: Selection Limit lewat Request Langsung Ditolak Tanpa Entri Changelog | Medium | Jejak audit: penolakan tidak boleh tercatat sebagai perubahan | Belum ada skrip | tidak |

## Yang Tidak Dinaikkan

- Mobile: E2E-017, E2E-018, E2E-019, E2E-139. Surface mobile belum dibangun.
- Guided tooltip: E2E-016.
- Notifikasi in-app [DEFERRED]: E2E-102, E2E-103, E2E-133. Fitur ditunda.
- Tampilan, sort, dan changelog: E2E-015, E2E-078, E2E-084, E2E-092, E2E-093, E2E-120, E2E-121.
- Download dan volume: E2E-088.

## Catatan untuk FE/QA

- Spek Target Berubah sejak Render (E2E-117 sampai E2E-137) menguji perlindungan data basi. Ini inti dari modul hak akses, jadi perlu dijaga.
- Naiknya spek notifikasi [DEFERRED] perlu ditunda sampai fitur notifikasi di-slicing.

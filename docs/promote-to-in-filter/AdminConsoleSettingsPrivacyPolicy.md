# Usulan Naik ke "Di Dalam Filter": Admin Console > Settings > Privacy Policy

Modul: Admin Console > Settings > Privacy Policy (Tabel Version History, Edit, Publish, Modal View, Editor, Idempotency Publish, Download, Android)
Sumber tabel: laporan progres e2e, scope `out` (luar filter), `AdminConsole/SettingsPrivacyPolicy`
Tanggal: 2026-11-13

## Kriteria

Spek dinaikkan ke "di dalam filter" bila dampak bisnisnya tinggi kalau spek itu benar-benar bug, tanpa melihat status run terakhir. Bila spek gagal karena kekurangan helper atau fitur belum dibangun, spek tetap diusulkan tapi ditandai di kolom Gap.

## Daftar Usulan Naik

| Spek | Judul | Prioritas | Alasan dampak bisnis | Status run | Gap |
|---|---|---|---|---|---|
| E2E-018 | Versi Active Berubah oleh Admin Lain Saat Modal Edit Dibuka atau Sedang Terbuka | High | Versi aktif yang berubah bisa menimpa publish dari admin lain | Lolos | tidak |
| E2E-032 | Idempotency Publish: Masa Berlaku Key 24 Jam dan Batas Tepat 24 Jam | Medium | Publish ganda bisa membuat dua versi aktif | Dilewati: fitur belum dibangun (tanpa rujukan) | ya (feature-gap:be, belum ada endpoint atau kontrak) |

## Yang Tidak Dinaikkan

- E2E-016, E2E-019: render modal 200 paragraf dan undo/redo editor. Tampilan dan aksesibilitas.
- E2E-036: overflow chip Published By. Tampilan.
- E2E-039: urutan tie-breaker versi. Tampilan.
- E2E-041: pagination dan preservasi state tabel. Tampilan.
- E2E-047: download CSV di atas 5.000 baris. Volume ekspor.
- E2E-056, E2E-057: Android. Surface mobile belum dibangun, jadi dikecualikan.

## Catatan untuk FE/QA

- E2E-032 belum bisa dijalankan karena endpoint idempotency publish belum ada. Naiknya baru berguna setelah BE menyediakan kontrak tersebut.

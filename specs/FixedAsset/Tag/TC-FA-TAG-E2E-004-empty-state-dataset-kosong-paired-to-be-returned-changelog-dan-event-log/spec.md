---
id: TC-FA-TAG-E2E-004-empty-state-dataset-kosong-paired-to-be-returned-changelog-dan-event-log
title: "Empty State Tab Paired, Tab To Be Returned, Modal Changelog, dan Modal Event Log Saat Dataset Kosong"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-15
  - TC-FA-TAG-85
  - TC-FA-TAG-939
  - TC-FA-TAG-1477
coverage:
  web: automated
---

# Empty State Tab Paired, Tab To Be Returned, Modal Changelog, dan Modal Event Log Saat Dataset Kosong

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat suite.md); spec ini tidak mengubahnya.
- State data yang dibutuhkan (dibentuk di hook `before` lewat fixture BE yang disediakan tim FE/BE; tidak ada endpoint yang didefinisikan di TC atau PRD yang dibaca): dalam scope akun Total Control tidak ada Tag Paired dan tidak ada aset Not Paired Yet (TC-FA-TAG-15), tidak ada Tag berstatus To Be Returned (TC-FA-TAG-85), tidak ada entri Changelog Tag (TC-FA-TAG-939), dan tidak ada entri Event Log To Be Returned (TC-FA-TAG-1477).
- State global yang diubah: data Tag, aset, Changelog, dan Event Log dalam scope Total Control dikosongkan sementara. Hook `after` (tetap jalan walau spec gagal) memulihkan seluruh data Pre-setup tab Paired dan tab To Be Returned lewat fixture BE yang sama; suite berjalan serial (`parallel: false`).
- Data Pre-setup yang dipulihkan: grup Excavator 20 Ton / Plant A, Excavator 20 Ton / Plant B, Laptop Pro 14 / HQ, Forklift Manual / Plant A; tab To Be Returned memuat Tag `RF-00071`, `RF-00088`, `NF-00092`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (ditandai untuk tim FE); data di atas dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Pemulihan idempotent. Nama dan kode literal tidak diberi suffix `{runId}` karena data Pre-setup yang dipulihkan harus sama persis (suite.md).

## Test Steps

### TC-FA-TAG-15: Empty state tab Paired saat belum ada Tag terpasang

1. Buka menu Fixed Asset > TAG lewat sidebar
2. Verifikasi Illustration tampil dengan judul `No paired TAG yet` dan deskripsi `TAGs appear here after they are paired to an asset.`
3. Verifikasi tabel grup tidak memuat baris

### TC-FA-TAG-939: Empty state Modal Changelog saat belum ada entri

4. Klik tombol `Changelog` pada Table Tools
5. Verifikasi Illustration tampil dengan judul `No changelog yet` dan deskripsi `Activities and changes will appear here.`
6. Klik ikon close pada Modal Changelog

### TC-FA-TAG-85: Empty state tab To Be Returned tanpa data

7. Klik Tab `To Be Returned`
8. Verifikasi ilustrasi tampil dengan judul `No TAG to be returned` dan deskripsi `TAGs removed from disposed assets will appear here.`
9. Verifikasi Badge pada Tab `To Be Returned` tetap tampil dan bernilai `0`

### TC-FA-TAG-1477: Modal Event Log tanpa entri menampilkan empty state ilustrasi, Title No event log yet, dan Description

10. Klik tombol `Event Log`
11. Verifikasi Modal berjudul `Event Log: To Be Returned` tampil
12. Verifikasi empty state tampil dengan ilustrasi, Title `No event log yet`, dan Description `Events appear here after TAGs leave the To Be Returned tab.` di bawah ilustrasi
13. Verifikasi empty state `No results found` tidak tampil
14. Klik ikon close pada Modal Event Log

## Notes

- Langkah 6 dan 14 adalah langkah penghubung (menutup modal), tanpa asersi (S-03).
- Urutan TC pada spec: TC-FA-TAG-15, 939, 85, 1477, agar pembukaan modal Changelog (tab Paired) tidak memerlukan pindah tab bolak-balik; tiap TC tetap mulai dari state yang sama.
- Langkah 13 adalah asersi absence atas empty state sementara; anchor positif adalah Verifikasi empty state `No event log yet` pada modal yang sama (langkah 12) (bagian 8b butir 2).
- Langkah 3 memakai empty state langkah 2 sebagai anchor positif bahwa surface sudah dimuat.
- Temuan untuk QA:
  - Mengosongkan seluruh data Tag dalam scope Total Control pada tenant uji bersama bersifat destruktif; mekanisme kosongkan dan pulihkan tidak didefinisikan di TC, PRD, atau LLD dan disediakan tim FE/BE (S-13). Mohon QA mengonfirmasi apakah tenant khusus (scope kosong) tersedia sebagai pengganti.
  - TC-FA-TAG-15 Precondition c, TC-FA-TAG-85, TC-FA-TAG-939, dan TC-FA-TAG-1477 tidak menyebut cara membentuk state kosong; spec menuliskannya sebagai kemampuan fixture BE tanpa endpoint karangan.
  - Tidak ada label tombol close yang disebut di TC untuk Modal Changelog dan Modal Event Log; spec memakai "ikon close" mengikuti konvensi modal.

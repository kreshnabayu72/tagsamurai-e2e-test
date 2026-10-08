---
id: TC-GS-POS-E2E-052-multi-konteks-realtime-sync-tabel-dan-filter-tanpa-reload
title: "Multi-Konteks: Record baru dan record terhapus dari sesi lain sinkron realtime tanpa reload, serta isolasi modal Edit"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-POS-175
  - TC-GS-POS-176
  - TC-GS-POS-278
  - TC-GS-POS-279
  - TC-GS-POS-297
coverage:
  web: automated
---

# Multi-Konteks: Record baru dan record terhapus dari sesi lain sinkron realtime tanpa reload, serta isolasi modal Edit

## Prerequisites

- Dua sesi browser simultan: Admin A mengamati tabel Position, Admin B melakukan mutasi

## Test Steps

### Sinkronisasi Realtime Record Baru & Hapus

1. Admin A membuka tab Position
2. Admin B membuat record Position baru "Cloud Engineer"
3. Verifikasi pada layar Admin A, record "Cloud Engineer" muncul di tabel secara realtime tanpa reload
4. Admin B menghapus record tersebut
5. Verifikasi pada layar Admin A, record otomatis menghilang dari tampilan

### Isolasi Modal Edit yang Terbuka

6. Admin A membuka modal Edit pada record "Procurement Specialist"
7. Admin B mengubah nama record tersebut menjadi "Sourcing Specialist" dari sesinya
8. Verifikasi form modal Edit yang sedang terbuka di layar Admin A tidak di-refresh sepihak oleh event SSE
9. Admin A menutup modal dan verifikasi tabel di layar Admin A menampilkan nama terbarukan

## Notes

- Menggabungkan sinkronisasi realtime tabel dan filter dari TC-GS-POS-175, 176, 278, 279, dan 297.
